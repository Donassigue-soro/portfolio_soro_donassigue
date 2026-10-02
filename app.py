"""Point d'entrée du portfolio : configuration, style, navigation."""
from __future__ import annotations

import streamlit as st

from components.navbar import build_navigation
from config.settings import CSS_FILES, SITE_ICON, SITE_TITLE
from utils.helpers import load_css

st.set_page_config(page_title=SITE_TITLE, page_icon=SITE_ICON, layout="wide", initial_sidebar_state="collapsed")
load_css(CSS_FILES)
build_navigation().run()
