"""Page CV (§17) : aperçu du PDF, téléchargement, liens. Le PDF reste la source officielle."""
from __future__ import annotations

import streamlit as st

from components._ui import page_header
from components.cta import render_cta
from components.footer import render_footer
from components.hero import read_cv_bytes
from data.profile import get_profile

p = get_profile()
page_header("CV", "Mon CV", "Le PDF ci-dessous est la version officielle de mon parcours.")

cv = read_cv_bytes(p.cv_path)
col_a, col_b, col_c = st.columns(3)
col_a.download_button("Télécharger le CV (PDF)", data=cv or b"", file_name="CV_Soro_Donassigue.pdf",
                      mime="application/pdf", disabled=cv is None, type="primary", use_container_width=True)
col_b.link_button("LinkedIn", p.linkedin_url, use_container_width=True)
col_c.link_button("GitHub", p.github_url, use_container_width=True)

if cv is None:
    st.info("Le CV n'est pas encore disponible. Ajoutez le fichier `assets/cv/cv.pdf`.")
else:
    try:  # st.pdf nécessite streamlit[pdf] (>= 1.49) : navigation et zoom intégrés
        st.pdf(cv, height=800)
    except Exception:  # extra absent ou version plus ancienne : le téléchargement reste disponible
        st.warning("L'aperçu n'est pas disponible dans cet environnement. Utilisez le bouton de téléchargement.")

render_cta("cv", include=("projects", "contact"))
render_footer()
