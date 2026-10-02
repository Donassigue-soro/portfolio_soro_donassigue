"""Fiche YOWL : projet full-stack, le code source est la démonstration (pas de démo embarquée)."""
from __future__ import annotations

import streamlit as st


def render_demo() -> None:
    """Précise au visiteur comment juger le projet."""
    st.caption("Projet full-stack (Laravel / Vue.js) : le dépôt GitHub est la meilleure démonstration.")
