from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emailservice.settings')

app = Celery('emailservice')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

