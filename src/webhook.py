import os
import requests


def send_webhook(content: str) -> bool:
    push_token = os.environ.get("PUSH_TOKEN", "")
    push_channel = os.environ.get("PUSH_CHANNEL", "pushplus")

    if not push_token:
        return False

    if push_channel == "pushplus":
        return _send_pushplus(push_token, content)
    elif push_channel == "serverchan":
        return _send_serverchan(push_token, content)
    return False


def _send_pushplus(token: str, content: str) -> bool:
    try:
        resp = requests.post(
            "http://www.pushplus.plus/send",
            json={
                "token": token,
                "title": "早报推送",
                "content": content,
                "template": "markdown",
            },
            timeout=10,
        )
        resp.raise_for_status()
        result = resp.json()
        return result.get("code") == 200
    except Exception:
        return False


def _send_serverchan(token: str, content: str) -> bool:
    try:
        resp = requests.post(
            f"https://sctapi.ftqq.com/{token}.send",
            data={
                "title": "早报推送",
                "desp": content,
            },
            timeout=10,
        )
        resp.raise_for_status()
        result = resp.json()
        return result.get("code") == 0
    except Exception:
        return False
