import os

from celery import Celery
import configurations

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compressor_configurations.settings')
os.environ['DJANGO_CONFIGURATION'] = 'BaseConf'

configurations.setup()

app = Celery('compressor_configurations')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
