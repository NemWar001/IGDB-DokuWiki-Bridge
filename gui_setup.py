# gui_setup.py
import tkinter as tk
from tkinter import filedialog
import webbrowser
import os

def render(frame):
    tk.Label(frame, text="🛠️ DokuWiki Setup", font=("Arial", 12, "bold")).pack(pady=10)

    # Schritt 1: Download-Link
    tk.Label(frame, text="1️⃣ DokuWiki herunterladen", font=("Arial", 10, "bold")).pack(pady=5)
    tk.Label(frame, text="Besuche die offizielle Download-Seite und wähle:", fg="gray", wraplength=700, justify="left").pack()
    tk.Label(frame, text="✔️ Include Web-Server\n✔️ Popular Plugins", fg="gray", justify="left").pack()

    def open_download_page():
        webbrowser.open("https://download.dokuwiki.org/")
    tk.Button(frame, text="🔗 Zur DokuWiki-Downloadseite", command=open_download_page).pack(pady=5)

    # Schritt 2: Lokale Instanz auswählen
    tk.Label(frame, text="2️⃣ Lokalen DokuWiki-Ordner auswählen", font=("Arial", 10, "bold")).pack(pady=10)
    status = tk.Label(frame, text="", fg="blue", wraplength=700, justify="left")
    status.pack(pady=5)

    def choose_folder():
        path = filedialog.askdirectory(title="DokuWiki-Ordner auswählen")
        if path:
            with open("dokuwiki_path.txt", "w", encoding="utf-8") as f:
                f.write(path)
            status.config(text=f"✔️ DokuWiki-Ordner gespeichert:\n{path}")
        else:
            status.config(text="⚠️ Kein Ordner ausgewählt")

    tk.Button(frame, text="📁 Ordner auswählen", command=choose_folder).pack(pady=5)

    # Schritt 3: Vorschau-URL anzeigen
    tk.Label(frame, text="3️⃣ Vorschau-URL", font=("Arial", 10, "bold")).pack(pady=10)

    def show_preview_url():
        try:
            with open("dokuwiki_path.txt", "r", encoding="utf-8") as f:
                path = f.read().strip()
            preview_url = "http://localhost/dokuwiki/doku.php?id=export:testspiel"
            tk.Label(frame, text=f"🔍 Vorschau-Link:\n{preview_url}", fg="green", wraplength=700).pack()
            webbrowser.open(preview_url)
        except FileNotFoundError:
            status.config(text="⚠️ Kein DokuWiki-Pfad gespeichert")

    tk.Button(frame, text="🌐 Vorschau öffnen", command=show_preview_url).pack(pady=5)
