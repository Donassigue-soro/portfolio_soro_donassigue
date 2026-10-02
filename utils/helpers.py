"""Fonctions utilitaires : chargement du CSS personnalisé."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import streamlit as st


@st.cache_data(show_spinner=False)
def _read_text(path: str, mtime: float) -> str:
    """Lit un fichier texte ; `mtime` invalide le cache si le fichier change."""
    return Path(path).read_text(encoding="utf-8")


def load_css(files: Iterable[Path]) -> None:
    """Injecte les feuilles de style dans la page."""
    css = "\n".join(_read_text(str(f), f.stat().st_mtime) for f in files if f.is_file())
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
