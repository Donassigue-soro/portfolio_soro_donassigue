"""Navigation principale : barre en haut via st.navigation (désactive la découverte automatique de pages/)."""
from __future__ import annotations

import streamlit as st
from streamlit.navigation.page import StreamlitPage

from utils.navigation import PAGES


def build_navigation() -> StreamlitPage:
    """Déclare les pages et retourne la page active (à exécuter avec .run())."""
    pages = [st.Page(p.path, title=p.title, icon=p.icon or None, default=p.default) for p in PAGES]
    return st.navigation(pages, position="top")
