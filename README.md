# bilibili-daily-email-bot

A GitHub Actions bot that fetches your Bilibili video stats (views & comments) daily, updates your outreach template automatically, and emails it to you every morning at 9am. No server needed.

每天早上9点自动抓取B站视频播放量和评论数，更新宣发文案数据，发送到你的邮箱。无需服务器，完全免费。

## 使用方法 How to use

1. Fork 这个仓库
2. 修改 `send_email.py` 里的视频BV号和文案模板
3. 在仓库 Settings → Secrets and variables → Actions 里添加：
   - `EMAIL`：你的163邮箱地址
   - `AUTH_CODE`：163邮箱的SMTP授权码
4. 在 Actions 里手动触发一次测试
5. 之后每天早上9点自动运行 ✅

## 效果示例

每天收到邮件，文案中的播放量和评论数自动更新为最新数据。

## 免费额度

GitHub Actions 每月免费 2000 分钟，本脚本每次运行约1分钟，完全够用。
一位独立游戏开发者&发行者拷打AI做的第一个脚本，希望大家不要嫌弃它太简单:）
