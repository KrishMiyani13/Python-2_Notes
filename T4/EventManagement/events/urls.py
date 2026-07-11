from django.urls import path
from events.views import home,add_event,view_event,login,signup

urlpatterns = [
    path('',home,name = 'home'),
    path('login/',login,name = 'login'),
    path('signup/',signup,name = ''),
    path('',home,name = 'home'),
    path('',home,name = 'home'),
]
