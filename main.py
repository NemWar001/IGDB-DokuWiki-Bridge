# main.py
import os
import csv
import json
import time
from urllib import request, error
from export_dokuwiki import format_with_template

def run_processing():
    # Lade Pfade und Konfiguration
    with open("selected_path.txt", "r", encoding="utf-8") as f:
        csv_path = f.read().strip()
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    with open("fields_config.txt", "r", encoding="utf-8") as f:
        fields = f.read().strip()

    CLIENT_ID = config["client_id"]
    ACCESS_TOKEN = config["access_token"]
    HEADERS = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    def igdb_search(game_name):
        url = "https://api.igdb.com/v4/games"
        query = f'search "{game_name}"; fields {fields}; limit 1;'
        data = query.encode("utf-8")
        req = request.Request(url, data=data, headers=HEADERS, method="POST")
        try:
            with request.urlopen(req) as response:
                return json.loads(response.read())
        except error.HTTPError as e:
            print(f"Fehler bei {game_name}: {e.code} – {e.reason}")
            return None

    os.makedirs("output", exist_ok=True)
    with open(csv_path, newline='', encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        title_index = headers.index("Title") if "Title" in headers else 0

        for i, row in enumerate(reader, start=1):
            if len(row) <= title_index:
                continue
            title = row[title_index].strip()
            if not title:
                continue
            result = igdb_search(title)
            if result:
                wiki_text = format_with_template(result[0])
                filename = title.replace(" ", "_").replace(":", "").lower()
                with open(f"output/{filename}.txt", "w", encoding="utf-8") as f:
                    f.write(wiki_text)
            print(f"[{i}] Verarbeitet: {title}")
            time.sleep(0.25)

def preview_game(title):
    from export_dokuwiki import format_with_template
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    with open("fields_config.txt", "r", encoding="utf-8") as f:
        fields = f.read().strip()

    CLIENT_ID = config["client_id"]
    ACCESS_TOKEN = config["access_token"]
    HEADERS = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://api.igdb.com/v4/games"
    query = f'search "{title}"; fields {fields}; limit 1;'
    data = query.encode("utf-8")
    req = request.Request(url, data=data, headers=HEADERS, method="POST")
    try:
        with request.urlopen(req) as response:
            result = json.loads(response.read())
            if result:
                return format_with_template(result[0])
    except Exception as e:
        return f"❌ Fehler: {e}"
    return "⚠️ Keine Daten gefunden"
