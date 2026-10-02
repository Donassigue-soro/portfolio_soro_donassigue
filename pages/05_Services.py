"""Page Services (§15) : offre freelance orientée besoin → solution → preuve."""
from __future__ import annotations

import streamlit as st

from components._ui import page_header
from components.cta import render_cta
from components.footer import render_footer
from components.service_card import render_service_card
from data.services import get_services

page_header("SERVICES", "Les problèmes que je peux résoudre",
            "Une offre pensée à partir de vos besoins, chaque service s'appuyant sur des projets réels.")

services = get_services()
for row in range(0, len(services), 2):
    for col, service in zip(st.columns(2), services[row:row + 2]):
        with col:
            render_service_card(service)

render_cta("services", include=("contact", "projects"))
render_footer()
