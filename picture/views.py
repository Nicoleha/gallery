from django.shortcuts import render
from django.http  import HttpResponse
from django.db import models
from .models import Image


def home(request):
    pics = Image.get_all()
    return render(request,'index.html',{"pics":pics})

def search_result(request):
    if 'image' in request.GET and request.GET['image']:
        search_ter = request.GET.get('image')
        searched = Image.search_image()


