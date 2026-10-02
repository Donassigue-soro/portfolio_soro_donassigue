"""Définition des pages de navigation (ordre, titre, fichier)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PageDef:
    """Une entrée de navigation."""
    title: str
    path: str
    icon: str = ""
    default: bool = False


PAGES: tuple[PageDef, ...] = (
    PageDef("Accueil", "pages/01_Accueil.py", ":material/home:", default=True),
    PageDef("Projets", "pages/02_Projets.py", ":material/data_object:"),
    PageDef("Compétences", "pages/03_Competences.py", ":material/build:"),
    PageDef("À propos", "pages/04_A_Propos.py", ":material/person:"),
    PageDef("Services", "pages/05_Services.py", ":material/business_center:"),
    PageDef("CV", "pages/06_CV.py", ":material/description:"),
    PageDef("Contact", "pages/07_Contact.py", ":material/mail:"),
)
