# gui_config.py
import tkinter as tk
from tkinter import filedialog

def render(frame):
    tk.Label(frame, text="⚙️ IGDB-Feldauswahl", font=("Arial", 12, "bold")).pack(pady=10)

    # Felder anzeigen
    try:
        with open("fields_config.txt", "r", encoding="utf-8") as f:
            current_fields = f.read().strip()
    except FileNotFoundError:
        current_fields = ""

    field_entry = tk.Text(frame, height=8, width=100)
    field_entry.insert("1.0", current_fields)
    field_entry.pack(pady=5)

    def save_fields():
        with open("fields_config.txt", "w", encoding="utf-8") as f:
            f.write(field_entry.get("1.0", "end").strip())
        status_fields.config(text="✔️ Felder gespeichert")

    tk.Button(frame, text="💾 Felder speichern", command=save_fields).pack()
    status_fields = tk.Label(frame, text="", fg="blue")
    status_fields.pack(pady=5)

    # Template-Auswahl
    tk.Label(frame, text="🧩 DokuWiki-Vorlage auswählen", font=("Arial", 12, "bold")).pack(pady=15)

    def choose_template():
        path = filedialog.askopenfilename(
            title="Template-Datei auswählen",
            filetypes=[("Textdateien", "*.txt")]
        )
        if path:
            with open("template_path.txt", "w", encoding="utf-8") as f:
                f.write(path)
            status_template.config(text=f"✔️ Template gespeichert:\n{path}")
        else:
            status_template.config(text="⚠️ Keine Datei ausgewählt")

    tk.Button(frame, text="📁 Template auswählen", command=choose_template).pack(pady=5)

    try:
        with open("template_path.txt", "r", encoding="utf-8") as f:
            current_template = f.read().strip()
    except FileNotFoundError:
        current_template = "Keine Vorlage gewählt"

    status_template = tk.Label(frame, text=f"Aktuelle Vorlage:\n{current_template}", fg="blue", wraplength=700, justify="left")
    status_template.pack(pady=5)
