# 微信早报机器人

每天 8:30 自动推送新闻、股票、虚拟币价格到个人微信。

## 快速开始

### 1. 获取推送 Token

选择以下任一推送服务（二选一）：

#### 方案 A: PushPlus (推荐)
1. 访问 https://www.pushplus.plus/
2. 微信扫码登录
3. 在个人中心复制 **Token**

#### 方案 B: Server酱
1. 访问 https://sct.ftqq.com/
2. 微信扫码登录
3. 在 SendKey 页面复制 **SendKey**

### 2. 配置 GitHub Secrets

在仓库 Settings → Secrets and variables → Actions 中添加：

| Secret 名称 | 值 | 必填 |
|------------|-----|------|
| `PUSH_TOKEN` | PushPlus Token 或 Server酱 SendKey | 是 |
| `PUSH_CHANNEL` | `pushplus` 或 `serverchan` | 否，默认 `pushplus` |

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
