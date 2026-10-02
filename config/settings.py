"""Réglages globaux de l'application."""
from __future__ import annotations

from pathlib import Path

ROOT: Path = Path(__file__).resolve().parent.parent
SITE_TITLE: str = "Soro Donassigué — Data Engineer & AI Developer"
SITE_ICON: str = "◆"
CSS_FILES: tuple[Path, ...] = (ROOT / "styles" / "custom.css", ROOT / "styles" / "components.css")
