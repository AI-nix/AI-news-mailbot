import smtplib
from email.mime.text import MIMEText
import os

def send_email(summary):
    msg = MIMEText(summary)
    msg['Subject'] = "[오늘의 AI 뉴스 요약]"
    msg['From'] = os.getenv("MAIL_FROM")
    msg['To'] = os.getenv("MAIL_TO")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(os.getenv("MAIL_FROM"), os.getenv("MAIL_PASS"))
        server.send_message(msg)
