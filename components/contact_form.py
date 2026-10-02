"""Formulaire de contact : validation, envoi SMTP via st.secrets, confirmation/erreur (§18)."""
from __future__ import annotations

import smtplib
import time
from email.message import EmailMessage

import streamlit as st

from utils.validators import validate_contact

COOLDOWN_S = 60  # anti-spam : un envoi par minute et par session


def _clean(value: str) -> str:
    """Supprime les retours à la ligne (anti header-injection) pour les champs d'en-tête."""
    return " ".join(value.split())


def send_email(name: str, email: str, subject: str, message: str) -> None:
    """Envoie le message. Identifiants lus dans st.secrets['smtp'] (host, port, user, password, to)."""
    cfg = st.secrets["smtp"]
    msg = EmailMessage()
    msg["Subject"] = f"[Portfolio] {_clean(subject)}"
    msg["From"] = cfg["user"]
    msg["To"] = cfg["to"]
    msg["Reply-To"] = _clean(email)
    msg.set_content(f"De : {_clean(name)} <{_clean(email)}>\n\n{message}")
    with smtplib.SMTP_SSL(cfg["host"], int(cfg.get("port", 465)), timeout=15) as server:
        server.login(cfg["user"], cfg["password"])
        server.send_message(msg)


def render_contact_form() -> None:
    """Affiche le formulaire et gère sa soumission."""
    with st.form("contact_form", clear_on_submit=False):
        name = st.text_input("Nom *", max_chars=100)
        email = st.text_input("Email *", max_chars=254)
        subject = st.text_input("Sujet *", max_chars=150)
        message = st.text_area("Message *", height=180, max_chars=3000)
        submitted = st.form_submit_button("Envoyer", type="primary")
    if not submitted:
        return
    wait = COOLDOWN_S - (time.time() - st.session_state.get("last_contact_sent", 0.0))
    if wait > 0:
        st.warning(f"Merci de patienter {int(wait)} s avant un nouvel envoi.")
        return
    errors = validate_contact(name, email, subject, message)
    if errors:
        for err in errors:
            st.error(err)
        return
    try:
        send_email(name, email, subject, message)
    except (KeyError, FileNotFoundError):
        st.error("L'envoi n'est pas configuré. Merci de me contacter directement par email ou LinkedIn.")
    except (smtplib.SMTPException, OSError):
        st.error("L'envoi a échoué. Réessayez plus tard ou contactez-moi directement.")
    else:
        st.session_state["last_contact_sent"] = time.time()
        st.success("Message envoyé, merci ! Je reviens vers vous rapidement.")
