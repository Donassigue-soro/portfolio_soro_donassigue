"""Métadonnées légères des projets (cahier des charges §9-13, §24-25).

Aucune donnée lourde ici : datasets et modèles sont chargés à la demande
dans projects/<id>/ lorsque la page du projet est ouverte.
Les champs vides (results, github, demo...) sont à compléter avec les éléments réels : rien n'est inventé.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import streamlit as st

CATEGORIES: tuple[str, ...] = ("Tous", "Data", "IA", "Software")  # filtres §9.2


@dataclass(frozen=True)
class Project:
    """Structure commune d'un projet (§24)."""
    id: str
    title: str
    category: str                      # "Data" | "IA" | "Software"
    positioning: str                   # ex. "Data Engineering / Analytics"
    description: str                   # description courte (carte projet)
    concept: str
    technologies: tuple[str, ...]
    image: str = ""                    # chemin relatif dans assets/ ou projects/<id>/assets/
    github: str = ""
    demo: str = ""
    context: str = ""
    problem: str = ""
    data_sources: tuple[str, ...] = ()
    solution: str = ""
    architecture: tuple[str, ...] = ()  # étapes affichées en flux vertical/horizontal
    pipeline: tuple[str, ...] = ()
    analysis: tuple[str, ...] = ()
    results: tuple[str, ...] = ()      # à compléter avec des résultats réels
    role: tuple[str, ...] = ()         # ce que le projet démontre
    features: dict[str, tuple[str, ...]] = field(default_factory=dict)
    to_confirm: str = ""               # point à vérifier avant publication


OLIST = Project(
    id="olist",
    title="Olist",
    category="Data",
    positioning="Data Engineering / Analytics",
    description="Pipeline Data et application analytique construits sur un dataset e-commerce brésilien.",
    concept="Transformation d'un dataset e-commerce brésilien en pipeline Data exploitable et application analytique.",
    technologies=("Python", "SQL", "dbt", "DuckDB", "Streamlit"),
    image="projects/olist/assets/Olist.png",
    demo="https://olistdash.streamlit.app/",
    context="Dataset e-commerce brésilien transformé en données exploitables pour l'analyse.",
    problem="Des données brutes éclatées en plusieurs tables, difficiles à exploiter directement pour l'analyse.",
    solution="Un pipeline dbt sur DuckDB, de la donnée brute jusqu'aux data marts, restitué dans un dashboard Streamlit.",
    architecture=("Raw Data", "dbt Staging", "Transformations", "Data Marts", "SQL Analytics", "Streamlit Dashboard"),
    pipeline=("Raw Data", "dbt Staging", "Transformations", "Data Marts", "SQL Analytics", "Streamlit Dashboard"),
    role=("Data Engineering", "SQL", "dbt", "Transformation de données", "Analytics", "Data Applications"),
    to_confirm="Ajouter métriques réelles (volumes, nombre de modèles dbt, KPIs) et liens GitHub / démo.",
)

AIRBNB = Project(
    id="airbnb",
    title="Inside Airbnb Barcelona",
    category="Data",
    positioning="Data Engineering / ELT",
    description="Traitement et transformation des données Inside Airbnb de Barcelone, en local avec dbt et DuckDB.",
    concept="Traitement et transformation des données Inside Airbnb de Barcelone avec une architecture locale basée sur dbt et DuckDB.",
    technologies=("Python", "SQL", "dbt Core", "DuckDB"),
    data_sources=("calendar.csv.gz", "listings.csv.gz", "reviews.csv.gz"),
    solution="Architecture ELT locale : chargement des fichiers compressés dans DuckDB puis modélisation avec dbt Core.",
    architecture=("Fichiers CSV.gz", "Chargement DuckDB", "Modèles dbt", "Données modélisées"),
    pipeline=("Fichiers CSV.gz", "Chargement DuckDB", "Modèles dbt", "Données modélisées"),
    role=("ETL / ELT", "Transformation SQL", "Modélisation", "dbt", "Traitement local de données",
          "Organisation d'un projet Data Engineering"),
    to_confirm="Vérifier les couches de modèles dbt réelles et ajouter les résultats.",
)

BOOKMATCH = Project(
    id="bookmatch",
    title="BookMatch AI",
    category="IA",
    positioning="AI Engineering / Recommendation System",
    description="Application de recommandation littéraire personnalisée selon le profil du lecteur.",
    concept="Application intelligente de recommandation littéraire personnalisée.",
    technologies=("Python", "TF-IDF", "SVD", "PostgreSQL", "Streamlit", "Machine Learning"),
    problem="La fatigue décisionnelle face à l'abondance de livres.",
    solution="Réduire la fatigue décisionnelle en proposant des correspondances littéraires adaptées au profil du lecteur.",
    features={
        "Moteur de recommandation": ("Analyse des préférences", "Genres", "Thèmes", "Style", "Humeur",
                                     "Historique de lecture", "Embeddings / Machine Learning",
                                     "Recommandations personnalisées"),
        "Profil utilisateur": ("Questionnaire d'appétence", "Rythme de lecture",
                               "Niveau de complexité", "Longueur souhaitée"),
        "Bibliothèque": ("À lire", "En cours", "Terminé", "Liste d'envies", "Fiches de livres"),
    },
    role=("Machine Learning", "Systèmes de recommandation", "NLP", "Application IA"),
    to_confirm="Ajouter l'architecture réelle, les métriques d'évaluation et une démo.",
)

YOWL = Project(
    id="yowl",
    title="YOWL",
    category="Software",
    positioning="Software Engineering / Full-Stack",
    description="Plateforme communautaire de partage, d'évaluation et de discussion autour de liens web.",
    concept="Plateforme communautaire centrée sur le partage, l'évaluation et la discussion autour de liens web.",
    technologies=("Laravel", "PHP", "Vue.js", "MySQL", "REST API"),
    features={
        "Interactions sociales": ("Publication d'URLs", "Commentaires filés", "Notation", "Réactions", "Upvote / downvote"),
        "Organisation et découverte": ("Catégories", "Tags", "Recherche", "Popularité", "Tendances", "Récence"),
        "Administration et modération": ("Utilisateurs", "Modérateurs", "Administrateurs", "Signalements",
                                         "Modération", "Tableau de bord d'administration"),
    },
    architecture=("Utilisateur", "Interface Vue.js", "REST API", "Laravel", "MySQL"),
    role=("Développement web", "Architecture frontend/backend", "API", "Base de données", "Logique métier",
          "Authentification / utilisateurs", "Rôles", "Modération"),
    to_confirm="Architecture à confirmer avec le repository réel avant publication (§13).",
)

# Registre central : ajouter un projet = l'ajouter ici + créer projects/<id>/project.py
ALL_PROJECTS: tuple[Project, ...] = (OLIST, AIRBNB, BOOKMATCH, YOWL)


@st.cache_data(show_spinner=False)
def get_projects(category: str = "Tous") -> tuple[Project, ...]:
    """Liste des projets, filtrée par catégorie ("Tous" = aucun filtre)."""
    if category == "Tous":
        return ALL_PROJECTS
    return tuple(p for p in ALL_PROJECTS if p.category == category)


def get_project(project_id: str) -> Project | None:
    """Retrouve un projet par identifiant."""
    return next((p for p in ALL_PROJECTS if p.id == project_id), None)


def projects_for_technology(tech: str) -> tuple[Project, ...]:
    """Projets utilisant une technologie donnée (lien technologies ↔ projets, §8.4)."""
    t = tech.lower()
    return tuple(p for p in ALL_PROJECTS if any(t in x.lower() or x.lower() in t for x in p.technologies))
