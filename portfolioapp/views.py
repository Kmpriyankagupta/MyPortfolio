from django.shortcuts import render

def index(request):
    return render(request,'app/index.html')

def testing(request):
    return render(request,'app/tesying.html')
