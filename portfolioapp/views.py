from django.shortcuts import render
from .models import *

def index(request):
    home = homepagedata.objects.all()
    
    return render(request,'app/index.html', {'home':home})

def testing(request):
    return render(request,'app/tesying.html')

def about(request):
    about = aboutpagedata.objects.all()
    return render(request,'app/about.html',{'about':about})
def services(request):
    return render(request,'app/services.html')
def contactt(request):
    contat = contact.objects.all()
    return render(request,'app/contact.html', {'contat':contat})
def blog(request):
    return render(request,'app/blog.html')
def testing(request):
    return render(request,'app/tesying.html')
def testing(request):
    return render(request,'app/tesying.html')
def testing(request):
    return render(request,'app/tesying.html')


