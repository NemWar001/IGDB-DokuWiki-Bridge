# gui_main.py
import tkinter as tk
import gui_import
import gui_twitch
import gui_config
import gui_export
import gui_setup
import gui_help

def start_gui():
    root = tk.Tk()
    root.title("🎮 IGDB → DokuWiki Bridge")
    root.geometry("900x700")

    # Menüleiste
    menubar = tk.Menu(root)

    # 📁 Datei-Menü
    menu_file = tk.Menu(menubar, tearoff=0)
    menu_file.add_command(label="CSV auswählen", command=lambda: show_view(gui_import.render))
    menubar.add_cascade(label="📁 Datei", menu=menu_file)

    # 🔧 Setup-Menü
    menu_setup = tk.Menu(menubar, tearoff=0)
    menu_setup.add_command(label="Twitch Zugangsdaten", command=lambda: show_view(gui_twitch.render))
    menu_setup.add_command(label="DokuWiki Setup", command=lambda: show_view(gui_setup.render))
    menubar.add_cascade(label="🔧 Setup", menu=menu_setup)

    # ⚙️ Konfiguration
    menu_config = tk.Menu(menubar, tearoff=0)
    menu_config.add_command(label="IGDB-Feldauswahl", command=lambda: show_view(gui_config.render))
    menubar.add_cascade(label="⚙️ Konfiguration", menu=menu_config)

    # 🚀 Verarbeitung
    menu_run = tk.Menu(menubar, tearoff=0)
    menu_run.add_command(label="Verarbeitung starten", command=lambda: show_view(gui_export.render))
    menubar.add_cascade(label="🚀 Export", menu=menu_run)

    # 📘 Hilfe
    menubar.add_command(label="📘 Hilfe", command=lambda: show_view(gui_help.render))

    root.config(menu=menubar)

    # Inhaltsbereich
    global content_frame
    content_frame = tk.Frame(root)
    content_frame.pack(fill="both", expand=True)

    def show_view(view_func):
        for widget in content_frame.winfo_children():
            widget.destroy()
        view_func(content_frame)

    # Startansicht
    show_view(gui_import.render)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
