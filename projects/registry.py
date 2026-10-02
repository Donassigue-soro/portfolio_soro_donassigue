"""Registre central des projets (§24).

Ajouter un cinquième projet = 1) déclarer sa fiche dans data/projects.py (ALL_PROJECTS),
2) créer projects/<id>/project.py avec une fonction render_demo(). Aucune autre page à modifier.
Les modules de démo sont importés à la demande : rien de lourd n'est chargé tant que la fiche n'est pas ouverte.
"""
from __future__ import annotations

import importlib
from pathlib import Path
from typing import Callable

from data.projects import ALL_PROJECTS, CATEGORIES, Project, get_project, get_projects

PROJECTS: tuple[Project, ...] = ALL_PROJECTS
PROJECTS_DIR = Path(__file__).resolve().parent

__all__ = ["PROJECTS", "CATEGORIES", "Project", "get_project", "get_projects", "load_demo", "assets_dir"]


def assets_dir(project_id: str) -> Path:
    """Dossier d'assets d'un projet (visuels, schémas)."""
    return PROJECTS_DIR / project_id / "assets"


def load_demo(project_id: str) -> Callable[[], None] | None:
    """Importe projects/<id>/project.py et retourne sa fonction render_demo (ou None si absente)."""
    try:
        module = importlib.import_module(f"projects.{project_id}.project")
    except ModuleNotFoundError as exc:
        if not (exc.name or "").startswith("projects"):
            raise  # dépendance manquante réelle : ne pas la masquer
        return None
    render = getattr(module, "render_demo", None)
    return render if callable(render) else None
