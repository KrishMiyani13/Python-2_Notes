from django.shortcuts import render
from .models import App
# Create your views here.
def app_details(requests,id):
    app = App.objects.get(id=id)
    return render(requests,'app_details.html',{'app':app})