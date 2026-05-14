from datetime import datetime, timezone, timedelta


CST = timezone(timedelta(hours=8))


def format_message(news: list, stocks: list, crypto: list) -> str:
    now = datetime.now(CST).strftime("%Y-%m-%d %H:%M")
    lines = [f"【早报推送】{now}\n"]

    if news:
        lines.append("📰 新闻")
        for i, item in enumerate(news, 1):
            title = item.get("title", "")
            url = item.get("url", "")
            if url:
                lines.append(f"{i}. [{title}]({url})")
            else:
                lines.append(f"{i}. {title}")
        lines.append("")

    if stocks:
        lines.append("📈 股票")
        for s in stocks:
            symbol = s["symbol"]
            price = s["price"]
            change = s["change_pct"]
            if price is not None:
                sign = "+" if change >= 0 else ""
                lines.append(f"{symbol}: {price} ({sign}{change}%)")
            else:
                lines.append(f"{symbol}: 数据获取失败")
        lines.append("")

    if crypto:
        lines.append("₿ 虚拟币")
        for c in crypto:
            name = c["name"].upper()
            price = c["price_usd"]
            change = c["change_24h"]
            sign = "+" if change >= 0 else ""
            lines.append(f"{name}: ${price:,.2f} ({sign}{change}%)")
        lines.append("")

    return "\n".join(lines)
