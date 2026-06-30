from django.urls import path
from students.views import home,login_user,logout_user,signup

urlpatterns = [
    path('',home,name = 'home'),
    path('login/',login_user,name = 'login'),
    path('signup/',signup,name = 'signup'),
    path('logout/',logout_user)
]
