"""Carte service : besoin → solutions → technologies → preuves (§15)."""
from __future__ import annotations

import streamlit as st

from components._ui import PAGE_PROJECTS, chips_html, esc, go_to, md_html
from data.projects import get_project
from data.services import Service


def render_service_card(service: Service) -> None:
    """Affiche un service avec accès direct à ses projets-preuves."""
    with st.container(key=f"pfcard_service_{service.id}"):
        md_html(f"""
        <h3 class="pf-card-title">{esc(service.title)}</h3>
        <p class="pf-need">« {esc(service.need)} »</p>
        <div class="pf-label pf-mono">Solutions</div>
        <ul class="pf-list">{"".join(f"<li>{esc(s)}</li>" for s in service.solutions)}</ul>
        <div class="pf-label pf-mono">Technologies</div>{chips_html(service.technologies)}""")
        projects = [p for pid in service.proof_project_ids if (p := get_project(pid))]
        st.caption("Preuves")
        if projects:
            for col, proj in zip(st.columns(len(projects)), projects):
                with col:
                    if st.button(proj.title, key=f"svc_{service.id}_{proj.id}", use_container_width=True):
                        go_to(PAGE_PROJECTS, selected_project=proj.id)
        if service.proof_note:
            st.caption(service.proof_note)
