from __future__ import absolute_import, unicode_literals
from celery import chain
from celery import shared_task
import time

@shared_task
def task1():
    print("in task1:")
    time.sleep(10)
    return True

@shared_task
def task2():
    print("in task2:")
    time.sleep(10)
    return True