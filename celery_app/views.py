from django.shortcuts import render,HttpResponse
from .tasks import func,send_mail_fun,enjoy
# Create your views here.
def testmail(request):
    func.delay()
    return HttpResponse('done views')



def sendmail(request):
    send_mail_fun.delay()
    return HttpResponse('mail sending...............')  



def enjoytask(request):
    enjoy.delay()
    return HttpResponse('all done task')        