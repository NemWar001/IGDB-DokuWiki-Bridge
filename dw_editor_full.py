import tkinter as tk
from tkinter import scrolledtext

# Dummy-Daten für Vorschau
dummy_data = {
    "title": "Chrono Trigger",
    "id": "12345",
    "summary": "Ein episches Zeitreise-Abenteuer.",
    "storyline": "Der Held reist durch die Zeit.",
    "release_date": "1995-03-11",
    "genres": "RPG, Adventure",
    "themes": "Zeitreise, Freundschaft",
    "game_modes": "Singleplayer",
    "perspectives": "Top-Down",
    "collection": "Chrono Collection",
    "franchise": "Chrono",
    "similar_games": "Final Fantasy VI, Secret of Mana",
    "platforms": "SNES",
    "companies": "Square",
    "rating": "9.5",
    "total_rating": "9.3",
    "age_rating": "USK 12",
    "cover": "{{wiki:dokuwiki-128.png}}",
    "screenshots": "{{screenshot1.jpg}}, {{screenshot2.jpg}}",
    "videos": "https://youtube.com/watch?v=xyz",
    "websites": "https://example.com"
}

# IGDB Platzhalter
igdb_placeholders = {
    "Titel": "{{title}}",
    "ID": "{{id}}",
    "Beschreibung": "{{summary}}",
    "Story": "{{storyline}}",
    "Release": "{{release_date}}",
    "Genres": "{{genres}}",
    "Themen": "{{themes}}",
    "Modi": "{{game_modes}}",
    "Perspektiven": "{{perspectives}}",
    "Sammlung": "{{collection}}",
    "Franchise": "{{franchise}}",
    "Ähnliche Spiele": "{{similar_games}}",
    "Plattformen": "{{platforms}}",
    "Firmen": "{{companies}}",
    "Bewertung": "{{rating}}",
    "Gesamtwertung": "{{total_rating}}",
    "Altersfreigabe": "{{age_rating}}",
    "Cover": "{{cover}}",
    "Screenshots": "{{screenshots}}",
    "Videos": "{{videos}}",
    "Webseiten": "{{websites}}"
}

def render_template(template: str, data: dict) -> str:
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template

class DWEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # DW-Toolbar
        toolbar = tk.Frame(self)
        toolbar.pack(fill="x", padx=5, pady=5)

        buttons = [
            ("B", lambda: self.insert_format("**", "**")),
            ("I", lambda: self.insert_format("//", "//")),
            ("U", lambda: self.insert_format("__", "__")),
            ("TT", lambda: self.insert_format("<code>", "</code>")),
            ("S", lambda: self.insert_format("<del>", "</del>")),
            ("Hh", lambda: self.insert_format("====== ", " ======")),
            ("H↓", self.insert_heading_menu),
            ("🔗", lambda: self.insert_text("[[Seitenname]]")),
            ("🌐", lambda: self.insert_text("[https://example.com|Text]")),
            ("1.", lambda: self.insert_text("- ")),
            ("•", lambda: self.insert_text("* ")),
            ("—", lambda: self.insert_text("----\n")),
            ("🖼️", lambda: self.insert_text("{{wiki:dokuwiki-128.png}}")),
            ("☺", lambda: self.insert_text(":)")),
            ("Ω", lambda: self.insert_text("§"))
        ]

        for label, cmd in buttons:
            tk.Button(toolbar, text=label, width=4, command=cmd).pack(side="left", padx=2)

        # Scrollbare IGDB-Leiste
        igdb_container = tk.Frame(self)
        igdb_container.pack(fill="x", padx=5, pady=(0,5))

        canvas = tk.Canvas(igdb_container, height=40)
        scrollbar = tk.Scrollbar(igdb_container, orient="horizontal", command=canvas.xview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar.set)

        canvas.pack(side="top", fill="x", expand=True)
        scrollbar.pack(side="bottom", fill="x")

        for label, code in igdb_placeholders.items():
            tk.Button(scroll_frame, text=label, command=lambda c=code: self.insert_text(c)).pack(side="left", padx=2)

        # Editorfeld
        self.editor = scrolledtext.ScrolledText(self, wrap="word", height=15)
        self.editor.pack(fill="both", expand=True, padx=5, pady=(0,5))

        # Vorschau-Button
        preview_btn = tk.Button(self, text="Vorschau aktualisieren", command=self.update_preview)
        preview_btn.pack(pady=5)

        # Vorschaufeld
        preview_label = tk.Label(self, text="Vorschau:")
        preview_label.pack(anchor="w", padx=5)

        self.preview = scrolledtext.ScrolledText(self, wrap="word", height=10, bg="#f0f0f0", state="disabled")
        self.preview.pack(fill="both", expand=True, padx=5, pady=(0,5))

    def insert_text(self, text):
        self.editor.insert(tk.INSERT, text)

    def insert_format(self, start, end):
        try:
            sel_start = self.editor.index("sel.first")
            sel_end = self.editor.index("sel.last")
            selected = self.editor.get(sel_start, sel_end)
            self.editor.delete(sel_start, sel_end)
            self.editor.insert(sel_start, f"{start}{selected}{end}")
        except tk.TclError:
            self.editor.insert(tk.INSERT, f"{start}{end}")

    def insert_heading_menu(self):
        popup = tk.Menu(self.master, tearoff=0)
        popup.add_command(label="H1", command=lambda: self.insert_format("====== ", " ======"))
        popup.add_command(label="H2", command=lambda: self.insert_format("===== ", " ====="))
        popup.add_command(label="H3", command=lambda: self.insert_format("==== ", " ===="))
        popup.add_command(label="H4", command=lambda: self.insert_format("=== ", " ==="))
        popup.add_command(label="H5", command=lambda: self.insert_format("== ", " =="))
        try:
            x = self.master.winfo_pointerx()
            y = self.master.winfo_pointery()
            popup.tk_popup(x, y)
        finally:
            popup.grab_release()

    def update_preview(self):
        template = self.editor.get("1.0", tk.END)
        rendered = render_template(template, dummy_data)
        self.preview.config(state="normal")
        self.preview.delete("1.0", tk.END)
        self.preview.insert(tk.END, rendered)
        self.preview.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DokuWiki Editor mit IGDB-Integration")
    root.geometry("1000x800")
    app = DWEditor(master=root)
    root.mainloop()
