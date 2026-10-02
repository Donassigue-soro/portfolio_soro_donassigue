"""Carte projet (§9.3) : catégorie, titre, description, technologies, visuel, bouton."""
from __future__ import annotations

from pathlib import Path

import streamlit as st

from components._ui import PAGE_PROJECTS, chips_html, esc, go_to, md_html
from data.projects import Project

ROOT = Path(__file__).resolve().parent.parent


def render_project_card(project: Project, key_prefix: str = "card") -> None:
    """Affiche une carte ; le bouton ouvre la fiche via session_state['selected_project']."""
    with st.container(key=f"pfcard_{key_prefix}_{project.id}"):
        image = ROOT / project.image if project.image else None
        if image and image.is_file():
            st.image(str(image), use_container_width=True)
        else:  # visuel de repli : bandeau dégradé avec le nom en mono
            md_html(f'<div class="pf-card-visual pf-mono">{esc(project.title)}</div>')
        md_html(f"""
        <div class="pf-card-cat pf-mono">{esc(project.category.upper())} · {esc(project.positioning)}</div>
        <h3 class="pf-card-title">{esc(project.title)}</h3>
        <p class="pf-card-desc">{esc(project.description)}</p>
        {chips_html(project.technologies)}""")
        if st.button("Explorer le projet", key=f"btn_{key_prefix}_{project.id}", use_container_width=True):
            go_to(PAGE_PROJECTS, selected_project=project.id)
