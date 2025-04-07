import os
import smtplib
from email.message import EmailMessage

def send_email(subject, text_body, html_body):
    mail_from = os.getenv("MAIL_FROM")
    mail_pass = os.getenv("MAIL_PASS")
    mail_to = os.getenv("MAIL_TO")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(mail_from, mail_pass)
        smtp.send_message(msg)

    print("📧 메일 보내기 완료!")
