# Cahier des charges — Portfolio Data Engineer & AI Developer

**Version :** 1.0  
**Date :** 2 octobre 2026  
**Technologie principale :** Streamlit / Python  
**Statut :** Cahier des charges fonctionnel et technique — prêt pour développement

---

## 1. Présentation du projet

Ce projet consiste à concevoir et développer un portfolio professionnel interactif sous **Streamlit**, destiné à présenter le profil, les compétences, les réalisations et les services de **Soro Donassigué Mathieu**.

Le portfolio poursuit deux objectifs complémentaires :

- **Emploi :** présenter clairement un profil orienté **Data Engineering & AI Development** aux recruteurs et entreprises.
- **Freelance :** présenter des problèmes que le profil peut résoudre, des solutions réalisables et des preuves techniques à travers des projets concrets.

Le portfolio ne doit pas être un simple CV en ligne. Il doit fonctionner comme une **vitrine technique interactive**, capable de démontrer les compétences à travers les réalisations.

---

# 2. Positionnement professionnel

## 2.1 Titre principal

> **Data Engineer & AI Developer**

## 2.2 Spécialités

> **Data Engineering • AI Engineering • Software Development**

## 2.3 Proposition de valeur

> **Je transforme les données brutes en pipelines fiables, analyses exploitables et applications concrètes.**

## 2.4 Fil conducteur

Le portfolio doit faire comprendre une chaîne de valeur cohérente :

```text
Données brutes
      ↓
Nettoyage & préparation
      ↓
ETL / ELT
      ↓
Données fiables
      ↓
Analyse / Analytics
      ↓
Machine Learning / IA
      ↓
Application / Dashboard

Le positionnement doit éviter de présenter le profil comme une accumulation de métiers indépendants. Le développement logiciel, le Machine Learning et la Data Science sont présentés comme des compétences complémentaires au cœur du parcours Data Engineering & AI.

3. Objectifs
3.1 Objectifs principaux

Le portfolio doit permettre à un visiteur de comprendre en moins de 30 secondes :

qui est le candidat ;
ce qu'il construit ;
quelles sont ses principales compétences ;
quels projets il a réalisés ;
comment le contacter.
3.2 Objectifs secondaires

Permettre à un visiteur technique d'explorer pendant plusieurs minutes :

les architectures ;
les pipelines ;
les technologies ;
les résultats ;
les démonstrations ;
les repositories GitHub.

Permettre à un prospect freelance de comprendre :

ses problèmes ;
les solutions proposées ;
les technologies utilisées ;
les réalisations servant de preuves.
4. Public cible

Le portfolio cible principalement :

Recruteurs / RH

Ils doivent pouvoir identifier rapidement :

le positionnement ;
les compétences ;
les projets ;
le CV ;
les moyens de contact.
Entreprises / responsables techniques

Ils doivent pouvoir explorer :

les architectures ;
les pipelines ;
les choix techniques ;
le code et les démonstrations.
Clients freelance

Ils doivent pouvoir identifier :

les problèmes pris en charge ;
les services proposés ;
les solutions possibles ;
les preuves concrètes.
5. Direction artistique
5.1 Style

Direction retenue :

Data / Tech Premium

Caractéristiques :

sombre ;
élégant ;
technique ;
minimaliste ;
professionnel ;
moderne ;
peu chargé ;
orienté Data / IA.

Éviter :

esthétique hacker cliché ;
vert néon dominant ;
animations excessives ;
effets 3D lourds ;
particules omniprésentes ;
musique ;
curseur personnalisé lourd.
5.2 Palette
Élément	Couleur
Background	#0B0F14
Secondary	#111827
Cards	#151D2A
Texte principal	#F8FAFC
Texte secondaire	#94A3B8
Accent principal	#38BDF8
Accent secondaire	#8B5CF6
5.3 Typographie
Inter : contenu principal.
JetBrains Mono : éléments techniques, labels, technologies et données.
6. Navigation

La navigation principale doit contenir :

SORO DONASSIGUÉ

Accueil
Projets
Compétences
À propos
Services
CV
Contact

[ Disponible pour opportunités ]

La navigation doit être :

claire ;
cohérente ;
responsive ;
facilement accessible ;
visuellement discrète.

Sur mobile, elle doit être remplacée par un menu adapté à la largeur disponible.

7. Architecture des pages

Le portfolio comporte les pages suivantes :

Accueil
Projets
Compétences
À propos
Services
CV
Contact
8. Page Accueil
8.1 Objectif

Présenter le profil et la proposition de valeur en quelques secondes.

8.2 Structure
Navbar
   ↓
Hero
   ↓
Stack technique
   ↓
Projets principaux
   ↓
Domaines d'expertise
   ↓
Parcours
   ↓
CTA final
   ↓
Footer
8.3 Hero

Contenu prévu :

DATA • IA • SOFTWARE

DATA ENGINEER & AI DEVELOPER

Je transforme les données brutes en pipelines fiables,
analyses exploitables et applications concrètes.

[ Explorer mes projets ]
[ Télécharger mon CV ]

Python • SQL • dbt • DuckDB • Machine Learning
Élément visuel

Une représentation discrète du pipeline :

RAW DATA → ETL / ELT → DATA → ANALYTICS / AI → APPLICATION
8.4 Stack technique

Afficher uniquement les technologies principales :

Python ;
SQL ;
dbt ;
DuckDB ;
Machine Learning ;
Streamlit ;
éventuellement Laravel / Vue selon le contexte.

Les technologies doivent pouvoir être associées aux projets correspondants.

8.5 Projets principaux

Afficher les quatre projets :

Olist
Inside Airbnb Barcelona
BookMatch AI
YOWL
8.6 Domaines d'expertise

Présenter :

Data Engineering ;
AI Engineering ;
Data Applications ;
Software Engineering.
8.7 CTA final

Le visiteur doit pouvoir accéder rapidement à :

projets ;
CV ;
contact.
9. Page Projets
9.1 Objectif

Démontrer les compétences à travers des réalisations concrètes.

9.2 Filtres
Tous | Data | IA | Software
9.3 Carte projet

Chaque carte contient :

catégorie ;
titre ;
description courte ;
technologies ;
visuel ;
bouton « Explorer le projet ».
9.4 Structure d'une fiche projet

Chaque projet doit suivre une structure homogène :

01 — CONTEXTE
02 — PROBLÈME
03 — DONNÉES
04 — SOLUTION
05 — ARCHITECTURE
06 — PIPELINE
07 — ANALYSE
08 — RÉSULTATS
09 — TECHNOLOGIES
10 — MON RÔLE
11 — CODE / DÉMONSTRATION

Toutes les sections ne sont pas obligatoires pour tous les projets : leur affichage dépend de la nature du projet.

10. Projet — Olist
Positionnement

Data Engineering / Analytics

Concept

Transformation d'un dataset e-commerce brésilien en pipeline Data exploitable et application analytique.

Stack principale
Python ;
SQL ;
dbt ;
DuckDB ;
Streamlit.
Pipeline
Raw Data
   ↓
dbt Staging
   ↓
Transformations
   ↓
Data Marts
   ↓
SQL Analytics
   ↓
Streamlit Dashboard
Rôle dans le portfolio

Olist constitue la démonstration principale des compétences en :

Data Engineering ;
SQL ;
dbt ;
transformation de données ;
Analytics ;
Data Applications.
11. Projet — Inside Airbnb Barcelona
Positionnement

Data Engineering / ELT

Concept

Projet de traitement et transformation des données Inside Airbnb de Barcelone avec une architecture locale basée sur dbt et DuckDB.

Données
calendar.csv.gz
listings.csv.gz
reviews.csv.gz
Technologies
Python ;
SQL ;
dbt Core ;
DuckDB.
Rôle dans le portfolio

Démontrer :

ETL / ELT ;
transformation SQL ;
modélisation ;
dbt ;
traitement local de données ;
organisation d'un projet Data Engineering.
12. Projet — BookMatch AI
Positionnement

AI Engineering / Recommendation System

Concept

Application intelligente de recommandation littéraire personnalisée.

Fonctionnalités
Moteur de recommandation
analyse des préférences ;
genres ;
thèmes ;
style ;
humeur ;
historique de lecture ;
embeddings / Machine Learning ;
recommandations personnalisées.
Profil utilisateur
questionnaire d'appétence ;
rythme de lecture ;
niveau de complexité ;
longueur souhaitée.
Bibliothèque
À lire ;
En cours ;
Terminé ;
liste d'envies ;
fiches de livres.
Valeur

Réduire la fatigue décisionnelle en proposant des correspondances littéraires adaptées au profil du lecteur.

Technologies connues du projet
Python ;
TF-IDF ;
SVD ;
PostgreSQL ;
Streamlit ;
Machine Learning / recommandation.
13. Projet — YOWL
Positionnement

Software Engineering / Full-Stack

Concept

Plateforme communautaire centrée sur le partage, l'évaluation et la discussion autour de liens web.

Fonctionnalités
Interactions sociales
publication d'URLs ;
commentaires filés ;
notation ;
réactions ;
upvote / downvote.
Organisation et découverte
catégories ;
tags ;
recherche ;
popularité ;
tendances ;
récence.
Administration et modération
utilisateurs ;
modérateurs ;
administrateurs ;
signalements ;
modération ;
tableau de bord d'administration.
Stack
Laravel ;
PHP / PHP POO ;
Vue.js ;
MySQL ;
REST API.
Architecture à présenter

À confirmer avec l'architecture réelle du repository avant publication :

Utilisateur
    ↓
Interface Vue.js
    ↓
REST API
    ↓
Laravel
    ↓
MySQL
Rôle dans le portfolio

Démontrer :

développement web ;
architecture frontend/backend ;
API ;
base de données ;
logique métier ;
authentification / utilisateurs ;
rôles ;
modération.
14. Page Compétences
Principe

Ne pas utiliser de pourcentages arbitraires.

Les compétences doivent être regroupées par domaine et reliées aux projets qui les démontrent.

14.1 Data Engineering
Technologies
Python ;
SQL ;
dbt Core ;
DuckDB ;
Apache Kafka ;
PostgreSQL ;
MySQL ;
Git ;
GitHub.
Compétences
nettoyage de données ;
ETL / ELT ;
transformation SQL ;
data modeling ;
pipelines ;
streaming ;
bases relationnelles.
Projets associés
Olist ;
Inside Airbnb.
14.2 AI Engineering & Machine Learning
Technologies
Python ;
Pandas ;
NumPy ;
scikit-learn ;
TensorFlow ;
Keras ;
Streamlit.
Compétences
préparation des données ;
Machine Learning ;
Deep Learning ;
NLP ;
systèmes de recommandation ;
TF-IDF ;
SVD ;
LSTM ;
applications IA.
Projet associé
BookMatch AI.
14.3 Data Applications
Technologies
Streamlit ;
Python ;
Pandas ;
SQL ;
Plotly.
Compétences
dashboards interactifs ;
visualisation ;
applications analytiques ;
exploration de données ;
restitution des résultats.
Projet associé
Olist.
14.4 Software Engineering
Backend
PHP ;
Laravel ;
PHP orienté objet ;
Inertia.js.
Frontend
JavaScript ;
Vue.js 3 ;
Vite.
Bases de données
MySQL ;
PostgreSQL.
Compétences
applications web ;
APIs ;
logique backend ;
frontend ;
bases de données ;
architecture client/serveur.
Projet associé
YOWL.
14.5 Systèmes & outils
Systèmes
Ubuntu Linux ;
CLI ;
SSH ;
administration système.
Versioning
Git ;
GitHub.
14.6 Robotique & STEM

Section secondaire afin de valoriser l'expérience de formateur sans brouiller le positionnement principal.

Technologies
BBC micro:bit ;
Scratch ;
Microsoft MakeCode ;
LEGO Education WeDo ;
Makeblock ;
Tinkercad ;
3D Slash.
Compétences
initiation à la programmation ;
robotique éducative ;
conception 3D ;
transmission STEM.
15. Page Services
Objectif

Présenter clairement les problèmes que le profil peut résoudre dans un contexte freelance.

15.1 Data Engineering
Besoin

Vous avez des données sales, dispersées ou difficiles à exploiter ?

Solutions
nettoyage ;
transformation ;
ETL / ELT ;
pipelines ;
automatisation ;
structuration des données.
Technologies
Python ;
SQL ;
dbt ;
DuckDB ;
Kafka ;
Git.
Preuves
Olist ;
Inside Airbnb.
15.2 Data Analytics & Dashboards
Besoin

Vous voulez suivre votre activité et mieux comprendre vos performances ?

Solutions
KPIs ;
analyses ;
dashboards ;
visualisation ;
outils de suivi.
Technologies
SQL ;
Python ;
Pandas ;
Streamlit ;
Plotly.
Preuve
Olist.
15.3 AI & Predictive Solutions
Besoin

Vous voulez anticiper certaines tendances, produire des prédictions ou automatiser une partie de l'analyse ?

Solutions
Machine Learning ;
systèmes de recommandation ;
modèles prédictifs ;
analyse de données ;
applications IA.
Technologies
Python ;
scikit-learn ;
TensorFlow / Keras selon le besoin ;
NLP / embeddings selon le projet.
Preuve
BookMatch AI ;
autres projets ML/streaming selon leur niveau de finalisation.
15.4 Web & Data Applications
Besoin

Vous avez besoin d'une présence en ligne ou d'une application métier ?

Solutions
applications web ;
APIs ;
interfaces ;
bases de données ;
applications orientées Data.
Technologies
Laravel ;
PHP ;
Vue.js ;
JavaScript ;
Python ;
SQL.
Preuve
YOWL.
16. Page À propos
16.1 Introduction

Présenter le profil comme un :

Développeur Data & IA, avec une expérience complémentaire en développement logiciel et en pédagogie STEM.

16.2 Parcours

Présenter sous forme de timeline :

BAC Scientifique
      ↓
MIAGE — Université Félix Houphouët-Boigny
      ↓
Développement Web / Software
      ↓
Formation Data & IA — EPITECH Coding Academy
      ↓
Projets Data / IA
      ↓
Data Engineering & AI Development

Les informations doivent rester cohérentes avec le CV officiel.

16.3 Manière de travailler

Principes à présenter :

Learning by doing ;
rigueur technique ;
résolution de problèmes ;
pédagogie ;
autonomie ;
documentation et versioning.
16.4 Évolution

Illustrer :

Développement logiciel
        ↓
Manipulation des données
        ↓
Data Analytics
        ↓
Data Engineering
        ↓
Machine Learning / IA
        ↓
Applications Data & IA
16.5 Recherche professionnelle

Je recherche des opportunités en Data Engineering et en développement Data/IA, notamment sur des projets où je peux concevoir des pipelines, structurer les données et développer des applications exploitant la donnée et l'IA.

16.6 Au-delà du code

Section courte pouvant mentionner :

robotique ;
STEM ;
fabrication numérique ;
impression 3D ;
pédagogie.

Les centres d'intérêt personnels ne doivent pas dominer la page.

17. Page CV
Objectif

Présenter le CV sans dupliquer son contenu dans le portfolio.

Fonctionnalités
aperçu du CV PDF ;
navigation dans le document ;
zoom ;
téléchargement ;
lien LinkedIn ;
lien GitHub.
CTA
Explorer mes projets
Me contacter

Le PDF reste la source officielle du CV.

18. Page Contact
Objectif

Permettre à un recruteur ou un prospect de prendre contact rapidement.

Formulaire

Champs :

Nom ;
Email ;
Sujet ;
Message.
Validation
champs obligatoires ;
validation email ;
contrôle du message ;
confirmation après envoi ;
message d'erreur en cas d'échec.
Contacts
Email ;
LinkedIn ;
GitHub ;
Abidjan, Côte d'Ivoire.
Parcours
Recruteur
Opportunité
    ↓
CV
    ↓
Projets
    ↓
Contact
Client
Besoin
    ↓
Services
    ↓
Projets / preuves
    ↓
Contact

Les secrets nécessaires à l'envoi d'emails ne doivent jamais être écrits en dur dans le code.

19. Footer

Footer minimaliste :

SORO DONASSIGUÉ
Data Engineer & AI Developer

Python • SQL • Data Engineering • AI • Software

GitHub · LinkedIn · Email

Abidjan, Côte d'Ivoire

© 2026 Soro Donassigué

Built with Python & Streamlit
20. Responsive Design

Le portfolio doit fonctionner sur :

desktop ;
laptop ;
tablette ;
mobile.
Desktop
navigation horizontale ;
contenu large ;
cartes en grille ;
visualisations larges.
Mobile
navigation compacte ;
cartes empilées ;
CTA adaptés ;
graphiques responsives ;
architecture de pipeline lisible ;
aucun débordement horizontal.
21. Interactions et micro-interactions

Les interactions doivent rester sobres.

Autorisé / recommandé
hover léger ;
élévation des cartes ;
changement subtil de bordure ;
transitions ;
apparition progressive ;
filtres de projets ;
graphiques interactifs ;
navigation fluide.
À éviter
animations permanentes ;
autoplay vidéo ;
curseur personnalisé lourd ;
particules excessives ;
effets 3D inutiles ;
animations bloquant la lecture.
22. Architecture technique
22.1 Vue générale
                         VISITEUR
                            │
                            ▼
                    ┌───────────────┐
                    │   Streamlit   │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          Pages         Components      Projects
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                     Data / Services
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
            Profile       Contact          CV
23. Arborescence technique

Structure recommandée :

portfolio/
│
├── app.py
│
├── pages/
│   ├── 01_Accueil.py
│   ├── 02_Projets.py
│   ├── 03_Competences.py
│   ├── 04_A_Propos.py
│   ├── 05_Services.py
│   ├── 06_CV.py
│   └── 07_Contact.py
│
├── components/
│   ├── navbar.py
│   ├── footer.py
│   ├── hero.py
│   ├── project_card.py
│   ├── project_detail.py
│   ├── skill_card.py
│   ├── service_card.py
│   ├── timeline.py
│   ├── contact_form.py
│   └── pipeline_visual.py
│
├── projects/
│   ├── __init__.py
│   ├── registry.py
│   │
│   ├── olist/
│   │   ├── project.py
│   │   ├── data/
│   │   └── assets/
│   │
│   ├── airbnb/
│   │   ├── project.py
│   │   └── assets/
│   │
│   ├── bookmatch/
│   │   ├── project.py
│   │   └── assets/
│   │
│   └── yowl/
│       ├── project.py
│       └── assets/
│
├── data/
│   ├── profile.py
│   ├── skills.py
│   ├── services.py
│   └── projects.py
│
├── assets/
│   ├── images/
│   ├── icons/
│   ├── cv/
│   │   └── cv.pdf
│   └── fonts/
│
├── styles/
│   └── custom.css
│
├── utils/
│   ├── navigation.py
│   ├── helpers.py
│   └── validators.py
│
├── config/
│   └── settings.py
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
24. Système de projets

Les projets doivent être gérés de manière modulaire.

Registry

Le portfolio doit disposer d'un registre central :

PROJECTS = [
    OLIST,
    AIRBNB,
    BOOKMATCH,
    YOWL,
]

Chaque projet doit pouvoir contenir :

id
title
category
description
technologies
image
github
demo
context
problem
solution
architecture
pipeline
analysis
results
role

L'objectif est de pouvoir ajouter un cinquième projet sans réécrire toute l'application.

25. Gestion des données

Deux catégories de données doivent être séparées.

Données légères
data/
├── profile.py
├── skills.py
├── services.py
└── projects.py

Elles peuvent être chargées rapidement.

Données lourdes

Les datasets ou modèles des projets ne doivent pas être chargés au démarrage.

Exemple :

Accueil
   ↓
aucun chargement Olist

Utilisateur ouvre Olist
   ↓
chargement des données Olist

Utiliser le cache Streamlit lorsque pertinent :

@st.cache_data

et, si nécessaire pour certaines ressources persistantes :

@st.cache_resource
26. Relation avec GitHub

Le portfolio ne doit pas devenir une copie des repositories.

Portfolio

Présente :

contexte ;
architecture ;
pipeline ;
résultats ;
visualisations ;
démonstration ;
technologies.
GitHub

Présente :

code ;
README ;
structure ;
historique ;
implémentation complète.

Architecture :

Portfolio
    │
    ├── Présentation
    ├── Démonstration
    └── Explication
           │
           ├── GitHub
           └── Live Demo
27. Performance
Principes
ne pas charger tous les datasets au démarrage ;
ne pas charger les modèles ML inutilisés ;
utiliser le cache ;
limiter les dépendances ;
séparer les données de l'interface ;
éviter les assets inutilement lourds ;
privilégier des composants réutilisables.

Le portfolio doit rester rapide malgré son caractère interactif.

28. Dépendances

Le requirements.txt doit rester minimal.

Base potentielle :

streamlit
pandas
numpy
plotly
duckdb
scikit-learn

Ajouter une dépendance uniquement si elle est réellement utilisée par le portfolio.

Par exemple, TensorFlow ne doit pas être installé uniquement parce qu'il apparaît dans les compétences si aucun composant du portfolio ne l'utilise.

29. Sécurité

Ne jamais stocker :

mots de passe ;
clés API ;
identifiants SMTP ;
tokens ;
credentials de services ;

directement dans le repository.

Utiliser les secrets de Streamlit / environnement de déploiement.

Le fichier local de secrets doit être exclu de Git.

30. Déploiement

Le portfolio doit être conçu pour un déploiement simple sur une plateforme compatible Streamlit, notamment Streamlit Community Cloud ou une infrastructure équivalente.

Le repository doit pouvoir être cloné puis déployé avec :

requirements.txt
app.py
pages/
components/
projects/
assets/
styles/

Les secrets doivent être configurés séparément du code source.

31. Principes architecturaux

Le projet doit respecter les principes suivants :

Modularité

Les composants réutilisables sont séparés des pages.

Maintenabilité

Les données de contenu ne doivent pas être mélangées inutilement avec la logique d'affichage.

Extensibilité

Un nouveau projet doit pouvoir être ajouté sans refonte globale.

Performance

Les données lourdes sont chargées à la demande.

Simplicité

Ne pas ajouter une technologie uniquement pour donner une apparence « professionnelle ».

Cohérence

Le portfolio doit rester centré sur :

Data → Engineering → AI → Software → Applications

32. UX cible
Parcours recruteur
Accueil
  ↓
Profil
  ↓
Projets
  ↓
Olist
  ↓
Architecture
  ↓
GitHub
  ↓
CV
  ↓
Contact
Parcours freelance
Accueil
  ↓
Services
  ↓
Projets
  ↓
Démonstration
  ↓
Contact
Parcours technique
Accueil
  ↓
Projets
  ↓
Architecture
  ↓
Pipeline
  ↓
Code / GitHub
  ↓
Autres projets
33. Critères d'acceptation

Le portfolio sera considéré comme fonctionnel lorsque :

 le positionnement Data Engineer & AI Developer est immédiatement compréhensible ;
 la navigation fonctionne sur desktop et mobile ;
 les quatre projets sont accessibles ;
 les projets sont filtrables par catégorie ;
 chaque projet possède une présentation structurée ;
 Olist possède une démonstration Data suffisamment détaillée ;
 BookMatch présente clairement la dimension IA ;
 YOWL présente clairement la dimension Software Engineering ;
 Airbnb démontre le travail Data Engineering / ELT ;
 les compétences sont reliées aux projets ;
 les services sont compréhensibles pour un prospect ;
 le CV est consultable et téléchargeable ;
 le formulaire de contact est fonctionnel ;
 GitHub et LinkedIn sont accessibles ;
 le site est responsive ;
 aucun secret n'est présent dans le repository ;
 les données lourdes ne sont pas chargées inutilement ;
 les composants sont suffisamment modulaires ;
 le portfolio conserve une cohérence visuelle sur toutes les pages.
34. Priorités de développement
Phase 1 — Fondations
 Initialisation Streamlit
 Arborescence
 Configuration
 CSS
 Navigation
 Design system
Phase 2 — Pages principales
 Accueil
 Projets
 Compétences
 À propos
 Services
 CV
 Contact
Phase 3 — Système de projets
 Registry
 Project cards
 Project detail
 Filtres
 Olist
 Airbnb
 BookMatch
 YOWL
Phase 4 — Interactivité
 Pipeline visuel
 Graphiques
 Filtres
 Micro-interactions
 Démonstrations
Phase 5 — Optimisation
 Cache
 Performance
 Responsive
 Accessibilité
 Vérification mobile
 Vérification desktop
Phase 6 — Déploiement
 GitHub
 Configuration secrets
 Déploiement
 Tests production
 Correction des erreurs
35. Vision finale

Le portfolio doit être perçu comme une application Data/Tech professionnelle, et non comme une simple page web personnelle.

Le visiteur doit progressivement comprendre :

                    SORO DONASSIGUÉ
                           │
                           ▼
              DATA ENGINEER & AI DEVELOPER
                           │
                           ▼
                DONNÉES BRUTES
                           │
                           ▼
                 DATA ENGINEERING
                           │
                           ▼
                    ANALYTICS
                           │
                           ▼
                       IA / ML
                           │
                           ▼
                    APPLICATIONS
                           │
                           ▼
              PROBLÈMES MÉTIERS RÉSOLUS

Le portfolio doit donc montrer les compétences plutôt que simplement les déclarer.

36. Règle directrice du projet

Chaque élément du portfolio doit avoir une fonction : présenter le profil, démontrer une compétence, expliquer une réalisation ou faciliter une prise de contact.

Tout élément qui n'apporte pas l'une de ces quatre valeurs doit être questionné avant d'être ajouté.
