from django.shortcuts import render,redirect

# Create your views here.
def home (request):
    return render (request,'home.html')
def login (request):
    return render (request,'login.html')
def signup (request):
    return render (request,'signup.html')
def view_event (request):
    return render (request,'view_event.html')
def add_event (request):
    return render (request,'add_event.html')
