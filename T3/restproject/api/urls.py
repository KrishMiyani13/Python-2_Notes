from django.urls import path
from .views import *

urlpatterns = [

    path('', home),

    path('players/', PlayerListCreate.as_view()),

    path('players/<int:pk>/', PlayerDetail.as_view()),
]