from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def Maaax(request):
    return HttpResponse("Hello, Maaax!")

def Fanice(request):
    return HttpResponse("Chalnade, Min County?")
