from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")
    #return HttpResponse("Hello,world!!!!!!")

def vlad(request):
    return HttpResponse("Hi, Vlad!")

def ana(request):
    return HttpResponse("Hi, Ana!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })
    #return HttpResponse(f"Hello, {name.capitalize()}!")