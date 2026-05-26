from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Home.html')
def contects(request):
    return render(request,'contect.html')
def about(request):
    return render(request,'About.html')