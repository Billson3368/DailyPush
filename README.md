# 微信早报机器人

每天 8:30 自动推送新闻、股票、虚拟币价格到企业微信群。

## 快速开始

### 1. 获取企业微信群机器人 Webhook URL

1. 打开企业微信，进入目标群聊
2. 点击群设置 → 群机器人 → 添加
3. 复制 Webhook 地址 (格式: `https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx`)

### 2. 配置 GitHub Secrets

在仓库 Settings → Secrets and variables → Actions 中添加：

| Secret 名称 | 值 |
|------------|-----|
| `WECHAT_WEBHOOK_URL` | 企业微信群机器人 Webhook URL |

### 3. 手动测试

在 Actions 页面点击 "Daily Morning Push" → "Run workflow" 即可手动触发测试。

## 自定义配置

### 修改关注股票

编辑 `src/stocks.py` 中的 `DEFAULT_STOCKS` 列表。

### 修改关注虚拟币

编辑 `src/crypto.py` 中的 `DEFAULT_COINS` 列表。

### 修改推送时间

编辑 `.github/workflows/daily-push.yml` 中的 cron 表达式。
当前 `30 0 * * *` = UTC 00:30 = 北京时间 08:30。
