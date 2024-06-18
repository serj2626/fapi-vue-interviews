from config import settings
from celery import Celery

celery = Celery(
    'tasks', 
    broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}',
    include=['users.tasks'])
