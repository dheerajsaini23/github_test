from __future__ import absolute_import
from celery import shared_task
from celery.contrib.methods import task
from django.http import HttpResponse
from time import sleep
from datetime import timedelta
from celery.task.schedules import crontab

from celery.decorators import periodic_task

@periodic_task(
               run_every=(crontab(minute='*/1')),
               name='Cel'
)


def Test():
    return "Executed"

def Cel(request):
    out = Test.delay()
    return HttpResponse(out.get())