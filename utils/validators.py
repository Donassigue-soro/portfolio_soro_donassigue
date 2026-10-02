"""Validation des entrées du formulaire de contact (regex, bibliothèque standard uniquement)."""
from __future__ import annotations

import re

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
MESSAGE_MIN, MESSAGE_MAX = 10, 3000


def is_valid_email(email: str) -> bool:
    """Vrai si l'adresse a un format plausible (sans espace ni saut de ligne)."""
    return bool(EMAIL_RE.fullmatch(email.strip())) and len(email) <= 254


def validate_contact(name: str, email: str, subject: str, message: str) -> list[str]:
    """Retourne la liste des erreurs de validation (vide si tout est correct)."""
    errors: list[str] = []
    if not name.strip():
        errors.append("Le nom est obligatoire.")
    if not email.strip():
        errors.append("L'email est obligatoire.")
    elif not is_valid_email(email):
        errors.append("L'adresse email n'est pas valide.")
    if not subject.strip():
        errors.append("Le sujet est obligatoire.")
    n = len(message.strip())
    if n < MESSAGE_MIN:
        errors.append(f"Le message doit contenir au moins {MESSAGE_MIN} caractères.")
    elif n > MESSAGE_MAX:
        errors.append(f"Le message ne doit pas dépasser {MESSAGE_MAX} caractères.")
    return errors
