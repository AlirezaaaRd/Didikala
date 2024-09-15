from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from mainapp.models import Banner

def index(request):
    context = {
        'banner_images' : Banner.objects.get(title = 'Main_banners').image_set.all()
    }
    return render(request , 'index.html' , context)

def messages(request):
    return render(request , 'index.html')



 
# Create your views here.
