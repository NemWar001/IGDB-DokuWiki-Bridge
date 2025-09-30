# export_dokuwiki.py
from datetime import datetime

def get_template_path():
    try:
        with open("template_path.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "template_dokuwiki.txt"

def format_with_template(game):
    template_path = get_template_path()

    def format_list(items):
        return ", ".join(
            str(v.get("name", v)) if isinstance(v, dict) else str(v)
            for v in items
        ) if items else ""

    def format_date(timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d") if timestamp else ""

    def format_media(url):
        return f"{{{{ {url} }}}}" if url else ""

    def format_links(sites):
        return "\n".join(f"- {s.get('url')}" for s in sites if s.get("url")) if sites else ""

    def format_screenshots(shots):
        return "\n".join(f"{{{{ {s.get('url')} }}}}" for s in shots if s.get("url")) if shots else ""

    def format_videos(videos):
        return "\n".join(f"https://www.youtube.com/watch?v={v.get('video_id')}" for v in videos if v.get("video_id")) if videos else ""

    def format_companies(companies):
        return ", ".join(
            c.get("company", {}).get("name", "")
            for c in companies if isinstance(c, dict)
        ) if companies else ""

    def format_age_rating(ratings):
        if not ratings:
            return ""
        values = [str(r.get("rating")) for r in ratings if isinstance(r, dict) and r.get("rating")]
        return ", ".join(values)

    try:
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        return "⚠️ Vorlage nicht gefunden."

    replacements = {
        "name": game.get("name", ""),
        "id": str(game.get("id", "")),
        "summary": game.get("summary", ""),
        "storyline": game.get("storyline", ""),
        "release_date": format_date(game.get("first_release_date")),
        "genres": format_list(game.get("genres")),
        "themes": format_list(game.get("themes")),
        "game_modes": format_list(game.get("game_modes")),
        "perspectives": format_list(game.get("player_perspectives")),
        "collection": game.get("collection", {}).get("name", ""),
        "franchise": game.get("franchise", {}).get("name", ""),
        "similar_games": format_list(game.get("similar_games")),
        "platforms": format_list(game.get("platforms")),
        "companies": format_companies(game.get("involved_companies")),
        "rating": str(game.get("rating", "")),
        "total_rating": str(game.get("total_rating", "")),
        "age_rating": format_age_rating(game.get("age_ratings")),
        "cover": format_media(game.get("cover", {}).get("url")),
        "screenshots": format_screenshots(game.get("screenshots")),
        "videos": format_videos(game.get("videos")),
        "websites": format_links(game.get("websites")),
    }

    for key, value in replacements.items():
        template = template.replace(f"{{{{{key}}}}}", value)

    return template
