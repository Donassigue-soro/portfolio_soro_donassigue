"""Fiche projet homogène (§9.4). Seules les sections renseignées sont affichées, numérotées dynamiquement."""
from __future__ import annotations

from typing import Callable

import streamlit as st

from components._ui import chips_html, esc, md_html
from components.pipeline_visual import render_pipeline
from projects.registry import Project, load_demo
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def _bullets(items: tuple[str, ...]) -> None:
    md_html(f'<ul class="pf-list">{"".join(f"<li>{esc(i)}</li>" for i in items)}</ul>')


def _text(value: str) -> None:
    md_html(f'<p class="pf-body">{esc(value)}</p>')


def _solution(p: Project) -> None:
    if p.solution:
        _text(p.solution)
    for group, items in p.features.items():
        md_html(f'<div class="pf-label pf-mono">{esc(group)}</div>{chips_html(items)}')


def _links(p: Project) -> None:
    """Boutons GitHub / démo (ignorés si vides) puis démonstration chargée à la demande."""
    cols = st.columns(4)
    if p.github:
        cols[0].link_button("Code sur GitHub", p.github, use_container_width=True)
    if p.demo:
        cols[1].link_button("Démo en ligne", p.demo, use_container_width=True)
    render_demo = load_demo(p.id)  # import à la demande : rien de lourd avant l'ouverture de la fiche
    if render_demo:
        render_demo()


def render_project_detail(project: Project) -> None:
    """Affiche l'en-tête puis les sections non vides de la fiche."""
    md_html(f"""
    <div class="pf-card-cat pf-mono">{esc(project.category.upper())} · {esc(project.positioning)}</div>
    <h1 class="pf-hero-title">{esc(project.title)}</h1>
    <p class="pf-hero-text">{esc(project.concept)}</p>""")
    # Aperçu du projet et accès direct au dashboard
    image = ROOT / project.image if project.image else None
    if image and image.is_file():
        st.image(str(image), use_container_width=True)
    if project.demo:
        st.link_button("Ouvrir le dashboard", project.demo, type="primary")
    sections: list[tuple[str, bool, Callable[[], None]]] = [
        ("Contexte", bool(project.context), lambda: _text(project.context)),
        ("Problème", bool(project.problem), lambda: _text(project.problem)),
        ("Données", bool(project.data_sources), lambda: md_html(chips_html(project.data_sources))),
        ("Solution", bool(project.solution or project.features), lambda: _solution(project)),
        ("Architecture", bool(project.architecture), lambda: render_pipeline(project.architecture)),
        ("Pipeline", bool(project.pipeline) and project.pipeline != project.architecture,
         lambda: render_pipeline(project.pipeline)),
        ("Analyse", bool(project.analysis), lambda: _bullets(project.analysis)),
        ("Résultats", bool(project.results), lambda: _bullets(project.results)),
        ("Technologies", bool(project.technologies), lambda: md_html(chips_html(project.technologies))),
        ("Mon rôle", bool(project.role), lambda: _bullets(project.role)),
        ("Code / Démonstration", True, lambda: _links(project)),
    ]
    for number, (title, _, render) in enumerate([s for s in sections if s[1]], start=1):
        md_html(f'<div class="pf-section-title"><span class="pf-mono">{number:02d}</span> — {esc(title.upper())}</div>')
        render()
