import sys

from src.news import fetch_news
from src.stocks import fetch_stocks
from src.crypto import fetch_crypto
from src.formatter import format_message
from src.webhook import send_webhook


def main():
    news = fetch_news()
    stocks = fetch_stocks()
    crypto = fetch_crypto()

    message = format_message(news, stocks, crypto)
    print(message)

    success = send_webhook(message)
    if success:
        print("推送成功")
    else:
        print("推送失败", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
