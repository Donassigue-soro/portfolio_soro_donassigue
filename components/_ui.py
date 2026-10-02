"""Briques UI partagées par les composants : échappement HTML, injection compacte, navigation, chips."""
from __future__ import annotations

from html import escape
from typing import Iterable

import streamlit as st

# Chemins des pages enregistrées dans st.navigation (cf. app.py / utils/navigation.py)
PAGE_HOME = "pages/01_Accueil.py"
PAGE_PROJECTS = "pages/02_Projets.py"
PAGE_SERVICES = "pages/05_Services.py"
PAGE_CV = "pages/06_CV.py"
PAGE_CONTACT = "pages/07_Contact.py"


def esc(value: object) -> str:
    """Échappe une valeur avant insertion dans du HTML (anti-injection)."""
    return escape(str(value), quote=True)


def md_html(markup: str) -> None:
    """Injecte du HTML. Les lignes sont aplaties : l'indentation ferait basculer Markdown en bloc de code."""
    st.markdown("".join(line.strip() for line in markup.splitlines()), unsafe_allow_html=True)


def chips_html(items: Iterable[str], extra_class: str = "") -> str:
    """Rend une liste de technologies/labels sous forme de chips (police mono)."""
    chips = "".join(f'<span class="pf-chip">{esc(i)}</span>' for i in items)
    return f'<div class="pf-chips {extra_class}">{chips}</div>'


def go_to(page: str, **state: object) -> None:
    """Navigue vers une page en posant éventuellement des valeurs dans session_state."""
    for key, value in state.items():
        st.session_state[key] = value
    st.switch_page(page)


def page_header(kicker: str, title: str, text: str = "") -> None:
    """En-tête standard d'une page : étiquette mono, titre et phrase d'introduction."""
    md_html(f"""
    <section class="pf-page-head">
      <div class="pf-kicker pf-mono">{esc(kicker)}</div>
      <h1 class="pf-h1">{esc(title)}</h1>
      {f'<p class="pf-hero-text">{esc(text)}</p>' if text else ''}
    </section>""")


def section_title(title: str, subtitle: str = "") -> None:
    """Titre de section avec filet d'accentuation."""
    sub = f'<p class="pf-muted">{esc(subtitle)}</p>' if subtitle else ""
    md_html(f'<h2 class="pf-h2">{esc(title)}</h2>{sub}')
