# Portfolio — Data Engineer & AI Developer

Portfolio interactif Streamlit (dark mode « Data / Tech Premium »).

## Lancer en local
```bash
python -m venv .venv && source .venv/bin/activate   # Windows : .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # puis le remplir
streamlit run app.py
```

## Structure
- `app.py` : point d'entrée · `pages/` : vues · `components/` : UI réutilisable
- `data/` : données légères (profil, compétences, services, projets)
- `projects/` : registre + démos par projet (chargées à la demande)
- `styles/` : CSS · `utils/` · `config/` · `assets/` (CV dans `assets/cv/cv.pdf`)

## À compléter avant publication
Liens GitHub/LinkedIn (`data/profile.py`), CV, résultats et visuels des projets, secrets SMTP.

## Déploiement
Streamlit Community Cloud : fichier principal `app.py`, secrets dans *Settings > Secrets*.
