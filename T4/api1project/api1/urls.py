from django.urls import path
from api1.views import public_view,private_view
urlpatterns = [
    path('public/',public_view,name="public_view"),
    path('private/',private_view,name="private_view")
]
