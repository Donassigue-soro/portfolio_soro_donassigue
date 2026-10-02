"""Page À propos (§16) : introduction, parcours, manière de travailler, évolution, recherche."""
from __future__ import annotations

import streamlit as st

from components._ui import chips_html, esc, md_html, page_header, section_title
from components.cta import render_cta
from components.footer import render_footer
from components.timeline import render_evolution, render_timeline
from data.profile import get_profile

p = get_profile()
page_header("À PROPOS", p.name, p.intro)

section_title("Parcours")
render_timeline(p.timeline)

col_a, col_b = st.columns(2)
with col_a:
    section_title("Manière de travailler")
    md_html(chips_html(p.work_principles))
with col_b:
    section_title("Évolution")
    render_evolution(p.evolution)

section_title("Recherche professionnelle")
md_html(f'<div class="pf-highlight">{esc(p.search_statement)}</div>')

# Section volontairement courte : les centres d'intérêt ne doivent pas dominer la page
section_title("Au-delà du code")
md_html(chips_html(p.beyond_code))

render_cta("about", include=("projects", "cv", "contact"))
render_footer()
