import os
import requests


def fetch_news() -> list[dict]:
    api_key = os.environ.get("NEWS_API_KEY", "")
    if not api_key:
        return []

    news_items = []
    params = {"country": "cn", "pageSize": 5, "apiKey": api_key}

    try:
        resp = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params=params,
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        for article in data.get("articles", [])[:5]:
            news_items.append({
                "title": article.get("title", ""),
                "url": article.get("url", ""),
            })
    except Exception:
        pass

    try:
        resp = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={"country": "us", "pageSize": 3, "apiKey": api_key},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        for article in data.get("articles", [])[:3]:
            news_items.append({
                "title": article.get("title", ""),
                "url": article.get("url", ""),
            })
    except Exception:
        pass

    return news_items
