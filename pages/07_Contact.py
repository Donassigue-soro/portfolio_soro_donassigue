"""Page Contact (§18) : formulaire sécurisé et coordonnées."""
from __future__ import annotations

import streamlit as st

from components._ui import esc, md_html, page_header
from components.contact_form import render_contact_form
from components.footer import render_footer
from data.profile import get_contact_email, get_profile

def _short(url: str) -> str:
    """Affiche une URL sans le protocole (ex. github.com/pseudo)."""
    return url.removeprefix("https://").removeprefix("http://").rstrip("/")

p = get_profile()
page_header("CONTACT", "Parlons de votre projet",
            "Recruteur ou client : écrivez-moi, je réponds rapidement.")

col_form, col_info = st.columns([3, 2], gap="large")
with col_form:
    render_contact_form()
with col_info:
    email = get_contact_email()
    lines = []
    if email:
        lines.append(("Email", f'<a href="mailto:{esc(email)}">{esc(email)}</a>'))
    lines += [
        ("LinkedIn", f'<a href="{esc(p.linkedin_url)}" target="_blank" rel="noopener">{esc(_short(p.linkedin_url))}</a>'),
        ("GitHub", f'<a href="{esc(p.github_url)}" target="_blank" rel="noopener">{esc(_short(p.github_url))}</a>'),
        ("Localisation", esc(p.location)),
        ("Statut", esc(p.availability)),
    ]
    md_html("".join(f'<div class="pf-contact-line"><span class="pf-mono">{k}</span><span>{v}</span></div>'
                    for k, v in lines))

render_footer()
