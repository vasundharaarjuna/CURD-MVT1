from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)
