# 微信早报机器人设计文档

## 1. 概述

通过企业微信群机器人 Webhook，每天 8:30 自动推送包含新闻、股票、虚拟币的早报消息。零成本部署在 GitHub Actions 上。

## 2. 技术栈

| 组件 | 选型 | 理由 |
|------|------|------|
| 语言 | Python 3.x | 生态丰富，API 客户端成熟 |
| 定时调度 | GitHub Actions cron | 免费、无需服务器 |
| 新闻源 | NewsAPI | 免费 100 次/天 |
| 股票源 | yfinance (Yahoo Finance) | 免费无需 Key |
| 虚拟币源 | CoinGecko API | 免费无需 Key |
| 推送渠道 | 企业微信群机器人 Webhook | 免费、稳定 |

## 3. 架构设计

```
GitHub Actions (08:30 CST)
    │
    ├── fetch_news() ──────────► NewsAPI ──────────┐
    ├── fetch_stocks() ────────► yfinance ─────────┤
    ├── fetch_crypto() ────────► CoinGecko API ────┤
    │                                              ▼
    └── format_message() ──► 拼接 Markdown ──► send_wechat_webhook()
```

## 4. 代码结构

```
wechat-morning-bot/
├── .github/workflows/
│   └── daily-push.yml      # GitHub Actions 定时任务
├── src/
│   ├── __init__.py
│   ├── news.py             # 新闻获取
│   ├── stocks.py           # 股票价格获取
│   ├── crypto.py           # 虚拟币价格获取
│   ├── formatter.py        # 消息格式化
│   └── webhook.py          # 企业微信 Webhook 发送
├── main.py                 # 入口脚本
├── requirements.txt        # Python 依赖
└── README.md               # 使用说明
```

## 5. 数据源详情

### 5.1 新闻 (NewsAPI)
- API: `https://newsapi.org/v2/top-headlines`
- 参数: `country=cn`, `category=general`, `pageSize=5`
- 备用: `country=us` 获取国际新闻

### 5.2 股票 (yfinance)
- 关注列表: 可配置
- 默认: `000300.SS` (沪深300), `000001.SS` (上证指数)
- 数据: 最新价、涨跌幅

### 5.3 虚拟币 (CoinGecko)
- API: `https://api.coingecko.com/api/v3/simple/price`
- 默认: `bitcoin`, `ethereum`
- 参数: `vs_currencies=usd&include_24hr_change=true`

## 6. 环境变量

| 变量名 | 说明 | 必填 |
|--------|------|------|
| `NEWS_API_KEY` | NewsAPI 密钥 | 是 |
| `WECHAT_WEBHOOK_URL` | 企业微信群机器人 Webhook URL | 是 |

## 7. 错误处理

- API 超时: 10 秒超时，超时后跳过该模块
- API 失败: 单模块失败不影响其他模块，消息中标注"数据获取失败"
- 空结果: 某模块无数据时不显示该板块

## 8. GitHub Actions 配置

- 触发: `cron: '30 0 * * *'` (UTC 00:30 = CST 08:30)
- 环境: Python 3.x
- 密钥: 通过 GitHub Secrets 注入环境变量
