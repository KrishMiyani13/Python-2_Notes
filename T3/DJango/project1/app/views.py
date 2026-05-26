from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<H1> Hello World </h1>")
def Python(request):
    return HttpResponse("<H1> Python Page </h1>")
def Java(request):
    return HttpResponse("<H1> Java Page </h1>")
def PhP(request):
    return HttpResponse("<H1> PhP Page </h1>")
