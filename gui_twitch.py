# gui_twitch.py
import tkinter as tk
import urllib.request
import json
import webbrowser

def render(frame):
    tk.Label(frame, text="🔧 Twitch API Einrichtung", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Label(frame, text="Client-ID:").pack()
    entry_id = tk.Entry(frame, width=60)
    entry_id.pack()

    tk.Label(frame, text="Client-Secret:").pack()
    entry_secret = tk.Entry(frame, width=60, show="*")
    entry_secret.pack()

    status = tk.Label(frame, text="", wraplength=700, fg="blue", justify="left")
    status.pack(pady=10)

    def open_console():
        webbrowser.open("https://dev.twitch.tv/console/apps")

    def fetch_token():
        client_id = entry_id.get().strip()
        client_secret = entry_secret.get().strip()
        if not client_id or not client_secret:
            status.config(text="⚠️ Bitte beide Felder ausfüllen")
            return

        url = f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
        req = urllib.request.Request(url, method="POST")
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read())
                token = data["access_token"]
                status.config(text=f"✔️ Token erhalten:\n{token}")
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump({"client_id": client_id, "access_token": token}, f, indent=2)
        except Exception as e:
            status.config(text=f"❌ Fehler: {e}")

    tk.Button(frame, text="Twitch Developer Console öffnen", command=open_console).pack(pady=5)
    tk.Button(frame, text="Access Token abrufen", command=fetch_token).pack(pady=5)
