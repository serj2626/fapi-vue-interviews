from celery import Celery

from app.config import settings

# celery = Celery(__name__, broker=settings.CELERY_BROKER_URL)