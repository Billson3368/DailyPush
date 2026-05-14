import os
import json
import requests


def send_webhook(content: str) -> bool:
    webhook_url = os.environ.get("WECHAT_WEBHOOK_URL", "")
    if not webhook_url:
        return False

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": content,
        },
    }

    try:
        resp = requests.post(
            webhook_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        resp.raise_for_status()
        result = resp.json()
        return result.get("errcode") == 0
    except Exception:
        return False
