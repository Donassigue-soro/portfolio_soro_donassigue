"""Démonstration Olist : explorateur de l'échantillon de données (marts) déposé dans projects/olist/data/."""
from __future__ import annotations

from pathlib import Path

from projects._common import render_data_explorer


def render_demo() -> None:
    """Appelée par la fiche projet uniquement. Silencieuse si aucun échantillon n'est fourni."""
    render_data_explorer(Path(__file__).parent / "data", key="olist")
