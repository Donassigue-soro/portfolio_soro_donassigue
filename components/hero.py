"""Section Hero de l'accueil (§8.3)."""
from __future__ import annotations

from pathlib import Path

import streamlit as st

from components._ui import PAGE_PROJECTS, chips_html, esc, go_to, md_html
from components.pipeline_visual import render_pipeline
from data.profile import get_profile

ROOT = Path(__file__).resolve().parent.parent


@st.cache_data(show_spinner=False)
def read_cv_bytes(relative_path: str) -> bytes | None:
    """Lit le PDF du CV (mis en cache). Retourne None s'il est absent."""
    path = ROOT / relative_path
    return path.read_bytes() if path.is_file() else None


def render_avatar(width: int = 280) -> None:
    """Photo de profil ronde ; repli sur les initiales si l'image est absente."""
    p = get_profile()
    photo = ROOT / p.photo_path
    with st.container(key="pf_avatar"):
        if photo.is_file():
            st.image(str(photo), width=width)
        else:
            initials = "".join(w[0] for w in p.name.split()[:2]).upper()
            md_html(f'<div class="pf-avatar-fallback pf-mono">{esc(initials)}</div>')


def render_hero() -> None:
    """Affiche le hero : texte et CTA à gauche, photo à droite, pipeline en dessous."""
    p = get_profile()
    col_text, col_photo = st.columns([3, 2], vertical_alignment="center", gap="large")
    with col_text:
        md_html(f"""
        <section class="pf-hero">
          <div class="pf-kicker pf-mono">{esc(p.hero_kicker)}</div>
          <h1 class="pf-hero-title">{esc(p.title.upper())}</h1>
          <p class="pf-hero-text">{esc(p.value_proposition)}</p>
        </section>""")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Explorer mes projets", type="primary", key="hero_projects", use_container_width=True):
                go_to(PAGE_PROJECTS)
        with c2:
            cv = read_cv_bytes(p.cv_path)
            st.download_button("Télécharger mon CV", data=cv or b"", file_name="CV_Soro_Donassigue.pdf",
                               mime="application/pdf", disabled=cv is None, key="hero_cv", use_container_width=True)
        md_html(chips_html(p.hero_stack, "pf-chips--hero"))
    with col_photo:
        render_avatar()
    render_pipeline(p.pipeline_steps, compact=True)