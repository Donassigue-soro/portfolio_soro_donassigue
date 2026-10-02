"""Carte de compétences par domaine, reliée aux projets (§14)."""
from __future__ import annotations

import streamlit as st

from components._ui import PAGE_PROJECTS, chips_html, esc, go_to, md_html
from data.projects import get_project
from data.skills import SkillDomain


def render_skill_card(domain: SkillDomain) -> None:
    """Affiche technologies, compétences et projets associés d'un domaine."""
    groups = "".join(
        f'<div class="pf-label pf-mono">{esc(name)}</div>{chips_html(techs)}'
        for name, techs in domain.technologies.items()
    )
    abilities = (f'<div class="pf-label pf-mono">Compétences</div>'
                 f'<ul class="pf-list">{"".join(f"<li>{esc(a)}</li>" for a in domain.abilities)}</ul>'
                 if domain.abilities else "")
    secondary = " pf-card--secondary" if domain.secondary else ""
    with st.container(key=f"pfcard_skill_{domain.id}"):
        md_html(f'<div class="pf-card-block{secondary}"><h3 class="pf-card-title">{esc(domain.title)}</h3>{groups}{abilities}</div>')
        projects = [p for pid in domain.project_ids if (p := get_project(pid))]
        if projects:
            st.caption("Démontré par")
            for col, proj in zip(st.columns(len(projects)), projects):
                with col:
                    if st.button(proj.title, key=f"skill_{domain.id}_{proj.id}", use_container_width=True):
                        go_to(PAGE_PROJECTS, selected_project=proj.id)
