"""Démo pédagogique BookMatch : illustre le principe TF-IDF → SVD → similarité cosinus sur un mini-catalogue."""
from __future__ import annotations

import numpy as np
import streamlit as st

# Mini-catalogue d'exemple (descriptions thématiques rédigées pour la démo, pas le catalogue réel du projet)
CATALOG: tuple[tuple[str, str], ...] = (
    ("Dune", "désert planète empire politique religion écologie science-fiction épique"),
    ("1984", "dystopie surveillance totalitarisme liberté propagande politique"),
    ("Le Petit Prince", "conte poésie enfance amitié voyage philosophie"),
    ("L'Étranger", "absurde existentialisme meurtre société solitude philosophie"),
    ("Fondation", "science-fiction empire galactique mathématiques histoire futur politique"),
    ("Les Misérables", "justice pauvreté rédemption histoire société france"),
    ("Le Seigneur des anneaux", "fantasy quête aventure anneau guerre amitié épique"),
    ("Sapiens", "histoire humanité essai évolution société anthropologie"),
    ("Le Comte de Monte-Cristo", "vengeance prison aventure justice histoire france"),
    ("Neuromancer", "cyberpunk hackers intelligence artificielle futur technologie science-fiction"),
)


@st.cache_resource(show_spinner=False)
def _latent_space() -> np.ndarray:
    """Construit (une seule fois) l'espace latent : TF-IDF puis SVD, vecteurs normalisés."""
    from sklearn.decomposition import TruncatedSVD  # imports tardifs : chargés uniquement si la démo est ouverte
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.preprocessing import normalize
    tfidf = TfidfVectorizer().fit_transform([desc for _, desc in CATALOG])
    return normalize(TruncatedSVD(n_components=5, random_state=42).fit_transform(tfidf))


def recommend(liked: list[int], top_k: int = 3) -> list[tuple[str, float]]:
    """Profil = moyenne des livres aimés ; classement par similarité cosinus, livres aimés exclus."""
    latent = _latent_space()
    profile = latent[liked].mean(axis=0)
    scores = latent @ profile / (np.linalg.norm(profile) or 1.0)
    ranked = [(CATALOG[i][0], float(scores[i])) for i in np.argsort(-scores) if i not in liked]
    return ranked[:top_k]


def render_demo() -> None:
    """Interface de la démo, derrière un toggle pour ne rien calculer tant qu'elle n'est pas demandée."""
    st.caption("Illustration du principe de recommandation sur un mini-catalogue d'exemple "
               "(TF-IDF → SVD → similarité cosinus). Ce n'est pas le moteur complet du projet.")
    if not st.toggle("Essayer la démo", key="bookmatch_demo"):
        return
    titles = [t for t, _ in CATALOG]
    picked = st.multiselect("Livres que vous avez aimés", titles, key="bookmatch_liked")
    if not picked:
        return
    for title, score in recommend([titles.index(t) for t in picked]):
        st.write(f"**{title}** · similarité {score:.2f}")
