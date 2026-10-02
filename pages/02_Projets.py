"""Page Projets (§9) : filtres + grille de cartes, ou fiche détaillée si un projet est sélectionné."""
from __future__ import annotations

import streamlit as st

from components._ui import page_header
from components.footer import render_footer
from components.project_card import render_project_card
from components.project_detail import render_project_detail
from projects.registry import CATEGORIES, get_project, get_projects

selected = st.session_state.get("selected_project")
project = get_project(selected) if selected else None

if project:
    if st.button("← Tous les projets", key="back_to_projects"):
        st.session_state.pop("selected_project", None)
        st.rerun()
    render_project_detail(project)
else:
    page_header("PROJETS", "Des projets qui prouvent le travail",
                "Du pipeline de données à l'application, chaque projet est documenté.")
    category = st.pills("Catégorie", CATEGORIES, selection_mode="single", default="Tous",
                        label_visibility="collapsed", key="project_filter") or "Tous"
    projects = get_projects(category)
    for row in range(0, len(projects), 2):
        for col, item in zip(st.columns(2), projects[row:row + 2]):
            with col:
                render_project_card(item, key_prefix="list")
render_footer()
