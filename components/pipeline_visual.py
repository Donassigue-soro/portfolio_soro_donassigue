"""Visuel de pipeline (RAW DATA → ETL/ELT → DATA → ANALYTICS/AI → APPLICATION), responsive."""
from __future__ import annotations

from typing import Sequence

from components._ui import esc, md_html


def pipeline_html(steps: Sequence[str], compact: bool = False, vertical: bool = False) -> str:
    """Construit le HTML du pipeline. Sur mobile, le CSS passe en colonne."""
    parts: list[str] = []
    for i, step in enumerate(steps):
        parts.append(f'<div class="pf-step">{esc(step)}</div>')
        if i < len(steps) - 1:
            parts.append('<div class="pf-arrow">→</div>')
    cls = "pf-pipeline" + (" pf-pipeline--compact" if compact else "") + (" pf-pipeline--vertical" if vertical else "")
    return f'<div class="{cls}">{"".join(parts)}</div>'


def render_pipeline(steps: Sequence[str], compact: bool = False, vertical: bool = False) -> None:
    """Affiche le pipeline dans la page."""
    md_html(pipeline_html(steps, compact, vertical))
