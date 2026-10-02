"""Footer minimaliste (§19)."""
from __future__ import annotations

from components._ui import esc, md_html
from data.profile import get_contact_email, get_profile


def render_footer() -> None:
    """Affiche le pied de page commun à toutes les pages."""
    p = get_profile()
    email = get_contact_email()
    links = [f'<a href="{esc(p.github_url)}" target="_blank" rel="noopener">GitHub</a>',
             f'<a href="{esc(p.linkedin_url)}" target="_blank" rel="noopener">LinkedIn</a>']
    if email:
        links.append(f'<a href="mailto:{esc(email)}">Email</a>')
    md_html(f"""
    <footer class="pf-footer">
      <div class="pf-footer-name">{esc(p.display_name)}</div>
      <div class="pf-footer-title">{esc(p.title)}</div>
      <div class="pf-mono pf-muted">{esc(p.footer_skills)}</div>
      <div class="pf-footer-links">{" · ".join(links)}</div>
      <div class="pf-muted">{esc(p.location)}</div>
      <div class="pf-muted pf-small">© 2026 Soro Donassigué Mathieu · Built with Python &amp; Streamlit</div>
    </footer>""")
