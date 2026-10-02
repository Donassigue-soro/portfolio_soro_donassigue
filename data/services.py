"""Offre freelance : besoin → solutions → technologies → preuves (cahier des charges §15)."""
from __future__ import annotations

from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class Service:
    """Un service proposé."""
    id: str
    title: str
    need: str
    solutions: tuple[str, ...]
    technologies: tuple[str, ...]
    proof_project_ids: tuple[str, ...]  # identifiants du registre des projets
    proof_note: str = ""  # précision éventuelle sur les preuves


SERVICES: tuple[Service, ...] = (
    Service(
        id="data-engineering",
        title="Data Engineering",
        need="Vous avez des données sales, dispersées ou difficiles à exploiter ?",
        solutions=("Nettoyage", "Transformation", "ETL / ELT", "Pipelines", "Automatisation", "Structuration des données"),
        technologies=("Python", "SQL", "dbt", "DuckDB", "Kafka", "Git"),
        proof_project_ids=("olist", "airbnb"),
    ),
    Service(
        id="analytics-dashboards",
        title="Data Analytics & Dashboards",
        need="Vous voulez suivre votre activité et mieux comprendre vos performances ?",
        solutions=("KPIs", "Analyses", "Dashboards", "Visualisation", "Outils de suivi"),
        technologies=("SQL", "Python", "Pandas", "Streamlit", "Plotly"),
        proof_project_ids=("olist",),
    ),
    Service(
        id="ai-predictive",
        title="AI & Predictive Solutions",
        need="Vous voulez anticiper certaines tendances, produire des prédictions ou automatiser une partie de l'analyse ?",
        solutions=("Machine Learning", "Systèmes de recommandation", "Modèles prédictifs",
                   "Analyse de données", "Applications IA"),
        technologies=("Python", "scikit-learn", "TensorFlow / Keras selon le besoin", "NLP / embeddings selon le projet"),
        proof_project_ids=("bookmatch",),
        proof_note="Autres projets ML / streaming selon leur niveau de finalisation.",
    ),
    Service(
        id="web-data-apps",
        title="Web & Data Applications",
        need="Vous avez besoin d'une présence en ligne ou d'une application métier ?",
        solutions=("Applications web", "APIs", "Interfaces", "Bases de données", "Applications orientées Data"),
        technologies=("Laravel", "PHP", "Vue.js", "JavaScript", "Python", "SQL"),
        proof_project_ids=("yowl",),
    ),
)


@st.cache_data(show_spinner=False)
def get_services() -> tuple[Service, ...]:
    """Retourne les services (mis en cache)."""
    return SERVICES
