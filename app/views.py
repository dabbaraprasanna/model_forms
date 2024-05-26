from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def insert_topic(request):
    d={'ETFO':TopicForm()}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic is created')
        else:
            return HttpResponse('not done')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    d={'EWFO':WebpageForm()}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage is created')
        else:
            return HttpResponse('there is error')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    d={'EAFO':AccessForm()}
    if request.method=='POST':
        AFDO=AccessForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('access is created')
        else:
            return HttpResponse('there is error')
    return render(request,'insert_access.html',d)