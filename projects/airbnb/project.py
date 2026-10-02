"""Démonstration Inside Airbnb Barcelona : explorateur d'un échantillon (listings, calendar, reviews)."""
from __future__ import annotations

from pathlib import Path

from projects._common import render_data_explorer


def render_demo() -> None:
    """Appelée par la fiche projet uniquement. Les fichiers complets (.csv.gz) ne doivent pas être versionnés."""
    render_data_explorer(Path(__file__).parent / "data", key="airbnb")
