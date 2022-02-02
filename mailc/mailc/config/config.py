from mailc.exceptions import MailCConfigError
import os
import json
import logging

log = logging.getLogger(__name__)

def load_config():
    """
    Load configurations for mailc
    If environment is django, then it loads configuration from django.conf.settings
    Else configurations are loaded from environment variables
    """
    try:
        from django.conf import settings
        return load_from_django_settings(settings)
    except ImportError as exc:
        return load_config_from_environment()

def load_from_django_settings(settings):
    """
    Load mailc configurations from django settings
    """
    if hasattr(settings, 'MAILC_EMAIL_BACKENDS'):
        return {
            "MAILC_EMAIL_BACKENDS": settings.MAILC_EMAIL_BACKENDS
        }
    else:
        raise MailCConfigError("Please add MAILC_EMAIL_BACKENDS in django settings")


def load_config_from_environment():
    """
    Load mailc configurations from environment variables
    """
    json_backends = os.getenv('MAILC_EMAIL_BACKENDS')
    try:
        backends = json.loads(json_backends)
        return {
            "MAILC_EMAIL_BACKENDS": backends
        }
    except (json.decoder.JSONDecodeError, TypeError) as e:
        log.exception(e)
        raise MailCConfigError("environment variable MAILC_EMAIL_BACKENDS should be JSON")
