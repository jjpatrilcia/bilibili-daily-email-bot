import requests
import smtplib
from email.mime.text import MIMEText
import os

# ==========================================
# 配置区域 - 请修改以下内容
# ==========================================
BILIBILI_BVID = "请替换为你的B站视频BV号"  # 例如：BV1hNo5BvE2e

# 文案模板 - 用 {view} 表示播放量，{reply} 表示评论数
TEMPLATE = """请编辑任意文案Please edit any text

发布至今播放量{view}，评论{reply}"""
# ==========================================

def get_bilibili_data(bvid):
    url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    data = res.json()
    view = data["data"]["stat"]["view"]
    reply = data["data"]["stat"]["reply"]
    return view, reply

def format_data(view, reply):
    view_w = round(view / 10000, 1)
    reply_10 = (reply // 10) * 10
    return f"破{view_w}w", f"{reply_10}+"

def send_email(content):
    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = "今日宣发文案"
    msg["From"] = os.environ["EMAIL"]
    msg["To"] = os.environ["EMAIL"]
    with smtplib.SMTP_SSL("smtp.163.com", 465) as server:
        server.login(os.environ["EMAIL"], os.environ["AUTH_CODE"])
        server.sendmail(os.environ["EMAIL"], os.environ["EMAIL"], msg.as_string())

def main():
    view, reply = get_bilibili_data(BILIBILI_BVID)
    view_str, reply_str = format_data(view, reply)
    content = TEMPLATE.replace("{view}", view_str).replace("{reply}", reply_str)
    send_email(content)
    print("邮件发送成功！")

if __name__ == "__main__":
    main()
