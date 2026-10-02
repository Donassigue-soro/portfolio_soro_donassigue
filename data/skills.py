"""Compétences regroupées par domaine et reliées aux projets (cahier des charges §14). Pas de pourcentages."""
from __future__ import annotations

from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class SkillDomain:
    """Un domaine de compétences."""
    id: str
    title: str
    technologies: dict[str, tuple[str, ...]]  # sous-groupe -> technologies
    abilities: tuple[str, ...]
    project_ids: tuple[str, ...] = ()
    secondary: bool = False  # section secondaire (Robotique & STEM)


SKILL_DOMAINS: tuple[SkillDomain, ...] = (
    SkillDomain(
        id="data-engineering",
        title="Data Engineering",
        technologies={"Technologies": ("Python", "SQL", "dbt Core", "DuckDB", "Apache Kafka",
                                       "PostgreSQL", "MySQL", "Git", "GitHub")},
        abilities=("Nettoyage de données", "ETL / ELT", "Transformation SQL", "Data modeling",
                   "Pipelines", "Streaming", "Bases relationnelles"),
        project_ids=("olist", "airbnb"),
    ),
    SkillDomain(
        id="ai-engineering",
        title="AI Engineering & Machine Learning",
        technologies={"Technologies": ("Python", "Pandas", "NumPy", "scikit-learn", "TensorFlow", "Keras", "Streamlit")},
        abilities=("Préparation des données", "Machine Learning", "Deep Learning", "NLP",
                   "Systèmes de recommandation", "TF-IDF", "SVD", "LSTM", "Applications IA"),
        project_ids=("bookmatch",),
    ),
    SkillDomain(
        id="data-applications",
        title="Data Applications",
        technologies={"Technologies": ("Streamlit", "Python", "Pandas", "SQL", "Plotly")},
        abilities=("Dashboards interactifs", "Visualisation", "Applications analytiques",
                   "Exploration de données", "Restitution des résultats"),
        project_ids=("olist",),
    ),
    SkillDomain(
        id="software-engineering",
        title="Software Engineering",
        technologies={
            "Backend": ("PHP", "Laravel", "PHP orienté objet", "Inertia.js"),
            "Frontend": ("JavaScript", "Vue.js 3", "Vite"),
            "Bases de données": ("MySQL", "PostgreSQL"),
        },
        abilities=("Applications web", "APIs", "Logique backend", "Frontend", "Bases de données",
                   "Architecture client/serveur"),
        project_ids=("yowl",),
    ),
    SkillDomain(
        id="systems-tools",
        title="Systèmes & outils",
        technologies={"Systèmes": ("Ubuntu Linux", "CLI", "SSH", "Administration système"),
                      "Versioning": ("Git", "GitHub")},
        abilities=(),
    ),
    SkillDomain(
        id="robotics-stem",
        title="Robotique & STEM",
        technologies={"Technologies": ("BBC micro:bit", "Scratch", "Microsoft MakeCode",
                                       "LEGO Education WeDo", "Makeblock", "Tinkercad", "3D Slash")},
        abilities=("Initiation à la programmation", "Robotique éducative", "Conception 3D", "Transmission STEM"),
        secondary=True,
    ),
)

# Stack affichée sur l'accueil (§8.4) ; le lien avec les projets est calculé dynamiquement.
HOME_STACK: tuple[str, ...] = ("Python", "SQL", "dbt", "DuckDB", "Machine Learning", "Streamlit", "Laravel / Vue")


@st.cache_data(show_spinner=False)
def get_skill_domains() -> tuple[SkillDomain, ...]:
    """Retourne les domaines de compétences."""
    return SKILL_DOMAINS


def get_domain(domain_id: str) -> SkillDomain | None:
    """Retrouve un domaine par son identifiant."""
    return next((d for d in SKILL_DOMAINS if d.id == domain_id), None)
