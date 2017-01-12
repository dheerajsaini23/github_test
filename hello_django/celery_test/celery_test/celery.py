from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

#set the celery default module in django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')

app = Celery('celery_test', broker='redis://localhost:6379/0',backend='cache+memcached://127.0.0.1:11211/')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)