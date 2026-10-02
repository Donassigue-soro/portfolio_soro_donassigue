"""Données de profil : identité, hero, parcours, liens et contact (cahier des charges §2, §8, §16, §18, §19)."""
from __future__ import annotations

from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class TimelineStep:
    """Une étape du parcours (page À propos)."""
    label: str
    detail: str = ""


@dataclass(frozen=True)
class ExpertiseDomain:
    """Un domaine d'expertise (page Accueil)."""
    title: str
    description: str
    icon: str


@dataclass(frozen=True)
class Profile:
    """Profil public. Aucune donnée sensible ici (l'email vient de st.secrets)."""
    name: str
    display_name: str
    title: str
    specialties: str
    tagline: str
    hero_kicker: str
    hero_stack: tuple[str, ...]
    value_proposition: str
    availability: str
    location: str
    github_url: str
    linkedin_url: str
    cv_path: str
    intro: str
    search_statement: str
    footer_skills: str
    pipeline_steps: tuple[str, ...]
    expertise: tuple[ExpertiseDomain, ...]
    timeline: tuple[TimelineStep, ...]
    evolution: tuple[str, ...]
    work_principles: tuple[str, ...]
    beyond_code: tuple[str, ...]
    photo_path: str = "assets/images/profile.png"


PROFILE = Profile(
    name="Soro Donassigué Mathieu",
    display_name="SORO DONASSIGUÉ",
    title="Data Engineer & AI Developer",
    specialties="Data Engineering • AI Engineering • Software Development",
    tagline="Je transforme les données brutes en pipelines fiables, analyses exploitables et applications concrètes.",
    hero_kicker="DATA • IA • SOFTWARE",
    hero_stack=("Python", "SQL", "dbt", "DuckDB", "Machine Learning"),
    value_proposition="Je transforme les données brutes en pipelines fiables, analyses exploitables et applications concrètes.",
    availability="Disponible pour opportunités",
    location="Abidjan, Côte d'Ivoire",
    # TODO : remplacer par vos vraies URLs avant publication
    github_url="https://github.com/Donassigue-soro",
    linkedin_url="https://www.linkedin.com/in/mathieu-soro/",
    cv_path="assets/cv/cv.pdf",
    intro="Développeur Data & IA, avec une expérience complémentaire en développement logiciel et en pédagogie STEM.",
    search_statement=(
        "Je recherche des opportunités en Data Engineering et en développement Data/IA, notamment sur des projets "
        "où je peux concevoir des pipelines, structurer les données et développer des applications exploitant la donnée et l'IA."
    ),
    footer_skills="Python • SQL • Data Engineering • AI • Software",
    pipeline_steps=("RAW DATA", "ETL / ELT", "DATA", "ANALYTICS / AI", "APPLICATION"),
    expertise=(
        ExpertiseDomain("Data Engineering", "Nettoyage, ETL / ELT, transformations SQL et pipelines fiables.", "database"),
        ExpertiseDomain("AI Engineering", "Machine Learning, NLP et systèmes de recommandation.", "cpu"),
        ExpertiseDomain("Data Applications", "Dashboards interactifs et applications analytiques.", "bar-chart"),
        ExpertiseDomain("Software Engineering", "Applications web, APIs et bases de données.", "code"),
    ),
    timeline=(
        TimelineStep("BAC Scientifique"),
        TimelineStep("MIAGE", "Université Félix Houphouët-Boigny"),
        TimelineStep("Développement Web / Software"),
        TimelineStep("Formation Data & IA", "EPITECH Coding Academy"),
        TimelineStep("Projets Data / IA"),
        TimelineStep("Data Engineering & AI Development"),
    ),
    evolution=(
        "Développement logiciel",
        "Manipulation des données",
        "Data Analytics",
        "Data Engineering",
        "Machine Learning / IA",
        "Applications Data & IA",
    ),
    work_principles=(
        "Learning by doing",
        "Rigueur technique",
        "Résolution de problèmes",
        "Pédagogie",
        "Autonomie",
        "Documentation et versioning",
    ),
    beyond_code=("Robotique", "STEM", "Fabrication numérique", "Impression 3D", "Pédagogie"),
)


@st.cache_data(show_spinner=False)
def get_profile() -> Profile:
    """Retourne le profil (mis en cache : donnée légère et immuable)."""
    return PROFILE


def get_contact_email() -> str:
    """Email public lu depuis st.secrets (jamais en dur). Chaîne vide si absent."""
    try:
        return str(st.secrets.get("contact", {}).get("public_email", "sorodonassigue491@gmail.com"))
    except Exception:  # secrets.toml absent en local
        return ""
