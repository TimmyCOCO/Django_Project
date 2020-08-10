from django.contrib import auth
from django.shortcuts import render

from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    list=BookInfo.objects.all()
    return render(request,'book/index.html', context={'title':'index',"booklist":list})

def detail(request, id):
    list=BookInfo.objects.get(id=id).heroinfo_set.all()
    return render(request, 'book/detail.html', context={'herolist':list})

def check(request):
    return HttpResponse(request.META.get('HTTP_USER_AGENT','unknown'))