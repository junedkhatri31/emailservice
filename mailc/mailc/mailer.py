import smtplib
import logging
from mailc.config.config import load_config

from mailc.exceptions import MailNotSentError

log = logging.getLogger(__name__)
config = load_config()

def _send_email(backend, message):
    """
    Underlying method that actually send message using smtplib
    Accepts backend configuration and message to be sent
    Message should be object of email.message.EmailMessage
    Returns weather it succeded or not
    """
    try:
        session = smtplib.SMTP(backend['HOST'], backend['PORT'])
        session.starttls()
        session.login(backend['USERNAME'], backend['PASSWORD'])
        session.send_message(message)
        session.quit()
        return True
    except smtplib.SMTPException as exception:
        log.exception(exception)
        return False


def send_email(message):
    """
    send_email accepts email.message.EmailMessage send the message with configured backends
    if one backend fails to deliver, it tries with other backend
    """
    backends = config['MAILC_EMAIL_BACKENDS']
    success = None
    for backend in backends:
        log.info(
            "Sending mail with host: %s user: %s",
            backend['HOST'],
            backend['USERNAME'],
        )
        success = _send_email(backend, message)
        if success:
            break
        else:
            log.error(
                "Host: %s user: %s has some issues with sending emails",
                backend['HOST'],
                backend['USERNAME'],
            )
    if not success:
        raise MailNotSentError
