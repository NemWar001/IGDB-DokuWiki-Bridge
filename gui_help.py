# gui_help.py
import tkinter as tk

def render(frame):
    tk.Label(frame, text="📘 Hilfe: Platzhalter für DokuWiki-Vorlagen", font=("Arial", 12, "bold")).pack(pady=10)

    info = """
Du kannst in deiner Vorlage-Datei (z. B. template_dokuwiki.txt) folgende Platzhalter verwenden. Diese werden automatisch durch die passenden IGDB-Daten ersetzt:

🎮 Basisdaten
  {{name}}               → Spielname
  {{id}}                 → IGDB-ID
  {{summary}}            → Kurzbeschreibung
  {{storyline}}          → Handlungsbeschreibung
  {{release_date}}       → Veröffentlichungsdatum (formatiert)

🧠 Inhalte & Kategorien
  {{genres}}             → Genres
  {{themes}}             → Themen
  {{game_modes}}         → Spielmodi
  {{perspectives}}       → Spielerperspektiven
  {{collection}}         → Sammlung
  {{franchise}}          → Franchise
  {{similar_games}}      → Ähnliche Spiele

🖥️ Plattformen & Technik
  {{platforms}}          → Plattformen
  {{companies}}          → Entwickler/Publisher

📊 Bewertungen
  {{rating}}             → Community-Bewertung
  {{total_rating}}       → Gesamtbewertung
  {{age_rating}}         → Altersfreigabe

🖼️ Medien
  {{cover}}              → Cover-Bild (DokuWiki-Syntax)
  {{screenshots}}        → Screenshots (Liste)
  {{videos}}             → YouTube-Links
  {{websites}}           → Webseiten

💡 Hinweis:
Du kannst die Platzhalter beliebig in deiner Vorlage platzieren. Nicht vorhandene Daten werden automatisch leer gelassen.
"""

    text = tk.Text(frame, wrap="word", width=100, height=40)
    text.insert("1.0", info)
    text.config(state="disabled")
    text.pack(padx=10, pady=10)
