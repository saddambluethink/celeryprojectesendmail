from __future__ import absolute_import, unicode_literals
from datetime import timezone
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
#from django_celery_beat.models import PeriodictTask
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_project.settings')

app=Celery('django_celery_project')

app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')
   
    #CELERY Beat settings

app.conf.beat_schedule={
    'send-mail-every-day-at-8':{
        'task':'celery_app.tasks.send_mail_fun',
        #'task':'send_mail_fun',
        'schedule':crontab(hour=18,minute=26),
    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("hey ")