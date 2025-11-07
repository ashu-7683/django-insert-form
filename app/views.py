from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETDFO=TopicDjForm()
    d={'ETDFO':ETDFO}
    if request.method=='POST':
        TDFDO=TopicDjForm(request.POST)
        if TDFDO.is_valid():
            topic_name=TDFDO.cleaned_data['topic_name']
            TTO=Topic.objects.get_or_create(topic_name=topic_name)
            if TTO[1]:
                return HttpResponse('Topic inserted successfully')
            else:
                return HttpResponse('Topic already exists')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWDFO=WebPageDjForm()
    d={'EWDFO':EWDFO}
    if request.method=='POST':
        WDFDO=WebPageDjForm(request.POST)
        if WDFDO.is_valid():
            TO=WDFDO.cleaned_data['topic_name']
            name=WDFDO.cleaned_data['name']
            url=WDFDO.cleaned_data['url']
            email=WDFDO.cleaned_data['email']
            TWO=WebPage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
            if TWO[1]:
                return HttpResponse('Webpage inserted successfully')
            else:
                return HttpResponse('Webpage already exists')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EADFO=AccessRecordDjForm()
    d={'EADFO':EADFO}
    if request.method=='POST':
        ADFDO=AccessRecordDjForm(request.POST)
        if ADFDO.is_valid():
            WO=ADFDO.cleaned_data['name']
            author=ADFDO.cleaned_data['author']
            date=ADFDO.cleaned_data['date']
            TAO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)
            if TAO[1]:
                return HttpResponse('AccessRecord inserted successfully')
            else:
                return HttpResponse('AccessRecord already exists')
    return render(request,'insert_accessrecord.html',d)


def insert_topic_mf(request):
    ETMFO=TopicMF()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TMFDO=TopicMF(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Topic inserted successfully using ModelForm')
        return HttpResponse('Invalid data')
    return render(request,'insert_topic_mf.html',d)

def insert_webpage_mf(request):
    EWMFO=WebPageMF()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=WebPageMF(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('Webpage inserted successfully using ModelForm')
        return HttpResponse('Invalid data')
    return render(request,'insert_webpage_mf.html',d)

def insert_accessrecord_mf(request):
    EAMFO=AccessRecordMF()
    d={'EAMFO':EAMFO}
    if request.method=='POST':
        AMFDO=AccessRecordMF(request.POST)
        if AMFDO.is_valid():
            AMFDO.save()
            return HttpResponse('AccessRecord inserted successfully using ModelForm')
        return HttpResponse('Invalid data')
    return render(request,'insert_accessrecord_mf.html',d)