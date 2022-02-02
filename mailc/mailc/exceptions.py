class MaxRetriesError(Exception):
    """
    This exception will be raised when mailc will exceeds settings.MAILC_MAX_RETRIES
    """

class MailNotSentError(Exception):
    """
    This exception will be raised when mail is not send by all provided configs
    """

class MailCConfigError(Exception):
    """
    This exception will be raised when environment variables are not correct
    """
