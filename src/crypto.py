import requests


DEFAULT_COINS = ["bitcoin", "ethereum"]


def fetch_crypto(coins: list[str] | None = None) -> list[dict]:
    coins = coins or DEFAULT_COINS
    ids = ",".join(coins)

    try:
        resp = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": ids,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()

        results = []
        for coin_id in coins:
            coin_data = data.get(coin_id, {})
            if coin_data:
                results.append({
                    "name": coin_id,
                    "price_usd": coin_data.get("usd", 0),
                    "change_24h": round(coin_data.get("usd_24h_change", 0), 2),
                })
        return results
    except Exception:
        return []
