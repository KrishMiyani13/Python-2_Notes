from django.urls import path
from api1.views import public_view,privet_view

urlpatterns = [
    path('public/',public_view,name='public_view'),
    path('privet/',privet_view,name='privet_view')
]
