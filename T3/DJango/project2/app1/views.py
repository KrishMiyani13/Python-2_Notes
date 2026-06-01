from django.shortcuts import render

# Create your views here.

# Home 
def home(request):
    return render (request,"home.html")

#About
def about(request):
    return render (request,"about.html")

#course
def course(request):
    return render (request,"course.html")

#Java
def java(request):
    return render (request,"java.html")

#Python

def python(request):
    return render (request,"python.html")