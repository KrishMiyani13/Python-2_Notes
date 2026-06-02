from django.urls import path
from app1.views import home,about,course

urlpatterns = [
    path('',home),
    path('about/',about,name='about'),
    path('course/',course,name='course'),
]