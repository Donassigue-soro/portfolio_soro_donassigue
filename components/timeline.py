"""Timeline verticale (parcours) et flux d'évolution (page À propos)."""
from __future__ import annotations

from typing import Sequence

from components._ui import esc, md_html
from components.pipeline_visual import render_pipeline
from data.profile import TimelineStep


def render_timeline(steps: Sequence[TimelineStep]) -> None:
    """Affiche le parcours sous forme de timeline verticale."""
    items = "".join(
        f'<div class="pf-tl-item"><div class="pf-tl-dot"></div><div>'
        f'<div class="pf-tl-label">{esc(s.label)}</div>'
        + (f'<div class="pf-tl-detail">{esc(s.detail)}</div>' if s.detail else "")
        + "</div></div>"
        for s in steps
    )
    md_html(f'<div class="pf-timeline">{items}</div>')


def render_evolution(steps: Sequence[str]) -> None:
    """Affiche l'évolution professionnelle (flux vertical)."""
    render_pipeline(steps, vertical=True)
