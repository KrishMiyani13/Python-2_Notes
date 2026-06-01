from django.urls import path

from app1.views import home,about,java,python,course

urlpatterns= [
    path('home/',home),
    path('about/',about),
    path('course/',course),
    path('course/java/',java),
    path('course/python/',python),
]