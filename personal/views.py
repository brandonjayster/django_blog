from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html')

#def name of page your adding

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','jayster@protonmail.com']})

def about(request):
    return render(request, 'personal/about.html')