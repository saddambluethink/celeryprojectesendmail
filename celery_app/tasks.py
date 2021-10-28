from django.conf import settings
from django.contrib.auth import get_user_model
import celery_app
from celery import shared_task
from celery_project.celery import app
from django.core.mail import send_mail


@app.task(bind=True)
def func(self):
    print("celery works")
    return "done"



    # send mail all user 
@app.task(bind=True)
def send_mail_fun(self):
    users=get_user_model().objects.all()
    print("celery works send mail all user")
    for user in users:
        print("celery works send mail",user.email)
        mail_subject="hi this is celery testing"
        message="congrats you are sortlisted your interview on 26/11/2021 10:00 AM"
        to_email=user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    print("celery works send mail all user")
    return "emai sent successfully"







@app.task(bind=True)
def enjoy(self):
    l=["saddam","khan","rahul",
    "mohan",'roy','fezan','khan',
    'jiya','rohan','rahul','sohil',
    'alikhan','saddam','diviya','sakib','rohan']
    for i in l:
        print(i)
    print("celery works properly")
    return "work done"