"""Page Accueil (§8) : hero, stack, projets, expertise, parcours, CTA final."""
from __future__ import annotations

import streamlit as st

from components._ui import esc, md_html, section_title
from components.cta import render_cta
from components.footer import render_footer
from components.hero import render_hero
from components.project_card import render_project_card
from components.timeline import render_timeline
from data.profile import get_profile
from data.projects import get_projects, projects_for_technology
from data.skills import HOME_STACK

profile = get_profile()

render_hero()

# --- Stack technique : chaque technologie est reliée aux projets qui l'utilisent (§8.4)
section_title("Stack technique", "Sélectionnez une technologie pour voir les projets associés.")
tech = st.pills("Technologie", HOME_STACK, selection_mode="single", label_visibility="collapsed", key="home_stack")
if tech:
    related = projects_for_technology(tech)
    if related:
        st.caption("Utilisée dans : " + " · ".join(p.title for p in related))
    else:
        st.caption("Pas encore de projet public associé à cette technologie.")

# --- Projets principaux (grille 2 x 2)
section_title("Projets principaux")
projects = get_projects()
for row in range(0, len(projects), 2):
    for col, project in zip(st.columns(2), projects[row:row + 2]):
        with col:
            render_project_card(project, key_prefix="home")

# --- Domaines d'expertise
section_title("Domaines d'expertise")
for col, domain in zip(st.columns(len(profile.expertise)), profile.expertise):
    with col:
        with st.container(key=f"pfcard_expertise_{domain.title.replace(' ', '_')}"):
            md_html(f'<h3 class="pf-card-title">{esc(domain.title)}</h3><p class="pf-card-desc">{esc(domain.description)}</p>')

# --- Parcours (version courte)
section_title("Parcours")
render_timeline(profile.timeline)

# --- CTA final
section_title("Travaillons ensemble")
render_cta("home")
render_footer()
