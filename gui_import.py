# gui_import.py
import tkinter as tk
from tkinter import filedialog

def render(frame):
    tk.Label(frame, text="📁 CSV-Datei auswählen", font=("Arial", 12, "bold")).pack(pady=10)

    status = tk.Label(frame, text="", fg="blue", wraplength=700, justify="left")
    status.pack(pady=5)

    def choose_csv():
        filepath = filedialog.askopenfilename(
            title="CSV-Datei auswählen",
            filetypes=[("CSV-Dateien", "*.csv"), ("Alle Dateien", "*.*")]
        )
        if filepath:
            status.config(text=f"✔️ Gewählt:\n{filepath}")
            with open("selected_path.txt", "w", encoding="utf-8") as f:
                f.write(filepath)
        else:
            status.config(text="⚠️ Keine Datei ausgewählt")

    tk.Button(frame, text="Datei auswählen", command=choose_csv).pack(pady=10)
