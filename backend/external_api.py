import requests

# SEARCH MOVIES & TV
def search_tvmaze(query):
    url = f"https://api.tvmaze.com/search/shows?q={query}"
    res = requests.get(url)

    results = []
    for item in res.json():
        show = item['show']
        results.append({
            "id": show['id'],
            "title": show['name'],
            "poster": show['image']['medium'] if show['image'] else "",
            "type": "tv"
        })

    return results


# SEARCH ANIME
def search_anime(query):
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=10"
    res = requests.get(url)

    results = []
    for a in res.json()['data']:
        results.append({
            "id": a['mal_id'],
            "title": a['title'],
            "poster": a['images']['jpg']['image_url'],
            "type": "anime"
        })

    return results

