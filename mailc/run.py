from mailc import send_email
from email.message import EmailMessage
import logging

# set up logging to file
logging.basicConfig(
    level=logging.INFO,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == '__main__':
    message = EmailMessage()
    message.set_content("Hello from smtplib")
    message['Subject'] = 'NewTestBCCtest'
    to_mails = ['xyz@example.com']
    message['From'] = 'abc@example.com'
    message['To'] = ', '.join(to_mails)
    send_email(message)
