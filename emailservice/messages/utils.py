from email.message import EmailMessage
import mailc
from celery import shared_task
from emailservice.ecelery import app

@app.task
def send_email_in_background(from_email, to_email, subject, message_text):
    message = EmailMessage()
    message['To'] = to_email
    message['From'] = from_email
    message['Subject'] = subject
    message.set_content(message_text)
    mailc.send_email(message)
