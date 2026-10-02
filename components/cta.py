"""Bandeau d'appels à l'action : projets, CV, contact (§8.7, §17)."""
from __future__ import annotations

import streamlit as st

from components._ui import PAGE_CONTACT, PAGE_CV, PAGE_PROJECTS, go_to


def render_cta(key: str, include: tuple[str, ...] = ("projects", "cv", "contact")) -> None:
    """Affiche les boutons d'accès rapide. `key` doit être unique par page."""
    actions = {
        "projects": ("Explorer mes projets", PAGE_PROJECTS),
        "cv": ("Voir mon CV", PAGE_CV),
        "contact": ("Me contacter", PAGE_CONTACT),
    }
    for col, name in zip(st.columns(len(include)), include):
        label, page = actions[name]
        with col:
            if st.button(label, key=f"cta_{key}_{name}", type="primary" if name == include[0] else "secondary",
                         use_container_width=True):
                go_to(page)
