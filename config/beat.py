import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("themagicai")
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.beat_schedule = {
#     'add-every-10-seconds': {
#         'task': 'orders.tasks.add',
#         'schedule': 10.0,
#         'args': (16, 16),
#     },
# }
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
