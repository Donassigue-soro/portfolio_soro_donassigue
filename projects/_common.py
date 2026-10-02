"""Outils partagés par les démos : explorateur de données chargé à la demande (DuckDB)."""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

PATTERNS = ("*.parquet", "*.csv", "*.csv.gz")
PREVIEW_ROWS = 5000


def find_datasets(data_dir: Path) -> list[Path]:
    """Liste les fichiers de données exploitables d'un dossier (vide s'il n'existe pas)."""
    if not data_dir.is_dir():
        return []
    return sorted({p for pattern in PATTERNS for p in data_dir.glob(pattern)})


def _reader(path: Path) -> str:
    """Fonction DuckDB adaptée au format du fichier."""
    return "read_parquet(?)" if path.suffix == ".parquet" else "read_csv_auto(?)"


@st.cache_data(show_spinner="Lecture du fichier…", max_entries=8)
def load_preview(path: str, mtime: float) -> pd.DataFrame:
    """Lit un aperçu (PREVIEW_ROWS lignes). `mtime` invalide le cache si le fichier change."""
    import duckdb  # import tardif : DuckDB n'est chargé que si l'explorateur est activé
    con = duckdb.connect(":memory:")
    try:
        return con.execute(f"SELECT * FROM {_reader(Path(path))} LIMIT {PREVIEW_ROWS}", [path]).df()
    finally:
        con.close()


@st.cache_data(show_spinner=False, max_entries=8)
def count_rows(path: str, mtime: float) -> int | None:
    """Nombre total de lignes (Parquet uniquement : métadonnées, donc instantané)."""
    if Path(path).suffix != ".parquet":
        return None
    import duckdb
    con = duckdb.connect(":memory:")
    try:
        return int(con.execute("SELECT COUNT(*) FROM read_parquet(?)", [path]).fetchone()[0])
    finally:
        con.close()


def _distribution(series: pd.Series) -> pd.Series:
    """Distribution d'une colonne : histogramme (numérique continu) ou top 20 des valeurs."""
    clean = series.dropna()
    if clean.empty:
        return pd.Series(dtype="int64")
    if pd.api.types.is_numeric_dtype(clean) and clean.nunique() > 20:
        counts = pd.cut(clean, bins=20).value_counts().sort_index()
        counts.index = counts.index.astype(str)
        return counts
    return clean.astype(str).value_counts().head(20)


def render_data_explorer(data_dir: Path, key: str) -> None:
    """Explorateur générique : aperçu, schéma et distribution. N'affiche rien si aucun fichier n'est présent."""
    files = find_datasets(data_dir)
    if not files:
        return
    st.caption("Échantillon de données du projet : chargé uniquement à la demande.")
    if not st.toggle("Explorer les données", key=f"{key}_explore"):
        return
    chosen = st.selectbox("Fichier", files, format_func=lambda p: p.name, key=f"{key}_file")
    mtime = chosen.stat().st_mtime
    df = load_preview(str(chosen), mtime)
    total = count_rows(str(chosen), mtime)
    c1, c2 = st.columns(2)
    c1.metric("Lignes", f"{total:,}".replace(",", " ") if total else f"≥ {len(df):,} (aperçu)".replace(",", " "))
    c2.metric("Colonnes", len(df.columns))
    st.dataframe(df.head(100), use_container_width=True)
    column = st.selectbox("Distribution d'une colonne", list(df.columns), key=f"{key}_col")
    dist = _distribution(df[column])
    if dist.empty:
        st.caption("Colonne vide dans l'échantillon.")
    else:
        st.bar_chart(dist)
