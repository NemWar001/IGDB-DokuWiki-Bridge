# gui_export.py
import tkinter as tk
import threading
import main
import os
import subprocess
import platform

def render(frame):
    tk.Label(frame, text="🚀 Verarbeitung starten", font=("Arial", 12, "bold")).pack(pady=10)

    status = tk.Label(frame, text="⏳ Bereit zur Verarbeitung", wraplength=700, fg="blue", justify="left")
    status.pack(pady=10)

    open_button = tk.Button(frame, text="📂 Ausgabeordner öffnen", command=open_output_folder)
    open_button.pack(pady=10)
    open_button.config(state="disabled")  # Wird erst nach Erfolg aktiviert

    def start():
        status.config(text="⏳ Verarbeitung läuft…")
        open_button.config(state="disabled")

        def threaded():
            try:
                main.run_processing()
                status.config(text="✅ Verarbeitung abgeschlossen. Dateien im 'output/'-Ordner.")
                open_button.config(state="normal")
            except Exception as e:
                status.config(text=f"❌ Fehler: {e}")
                open_button.config(state="disabled")

        threading.Thread(target=threaded).start()

    tk.Button(frame, text="Verarbeitung starten", command=start).pack(pady=10)

def open_output_folder():
    output_path = os.path.abspath("output")
    if platform.system() == "Windows":
        subprocess.run(["explorer", output_path])
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", output_path])
    else:  # Linux
        subprocess.run(["xdg-open", output_path])
