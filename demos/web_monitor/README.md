# Web Monitor Mini Demo

用途：监控网页内容变化，变化时输出提醒内容。可改成 Telegram / Email / Slack 通知。

## 客户场景
- 监控商品价格/库存
- 监控竞品页面变化
- 监控公告/招聘/新闻更新

## 交付范围
- 定时抓取 URL
- 提取文本
- 保存 hash
- 内容变化时提示
- 错误日志

## 报价
49-149U，按目标页面复杂度调整。

## 运行
```bash
python3 web_monitor.py --url https://example.com --state state.json
```
