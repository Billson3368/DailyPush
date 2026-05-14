import requests


def fetch_news() -> list[dict]:
    news_items = []

    try:
        resp = requests.get(
            "https://top.baidu.com/board?tab=realtime",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            },
            timeout=10,
        )
        resp.raise_for_status()

        import json
        import re

        match = re.search(r'<!--s-data:(.*?)-->', resp.text, re.DOTALL)
        if match:
            data = json.loads(match.group(1))
            for item in data.get("cards", [{}])[0].get("content", [])[:10]:
                news_items.append({
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                })
    except Exception:
        pass

    if not news_items:
        try:
            resp = requests.get(
                "https://weibo.com/ajax/side/hotSearch",
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            for item in data.get("realtime", [])[:10]:
                title = item.get("word")
                if title:
                    news_items.append({
                        "title": title,
                        "url": f"https://s.weibo.com/weibo?q={title}",
                    })
        except Exception:
            pass

    return news_items
