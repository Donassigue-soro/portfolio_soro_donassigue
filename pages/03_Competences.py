"""Page Compétences (§14) : domaines reliés aux projets, sans pourcentages."""
from __future__ import annotations

import streamlit as st

from components._ui import page_header, section_title
from components.cta import render_cta
from components.footer import render_footer
from components.skill_card import render_skill_card
from data.skills import get_skill_domains

page_header("COMPÉTENCES", "Ce que je maîtrise, et où je l'ai prouvé",
            "Chaque domaine est relié aux projets qui le démontrent.")

domains = get_skill_domains()
main = [d for d in domains if not d.secondary]
for row in range(0, len(main), 2):
    for col, domain in zip(st.columns(2), main[row:row + 2]):
        with col:
            render_skill_card(domain)

secondary = [d for d in domains if d.secondary]
if secondary:
    section_title("Au-delà du code")  # section secondaire : Robotique & STEM
    for domain in secondary:
        render_skill_card(domain)

render_cta("skills", include=("projects", "contact"))
render_footer()
