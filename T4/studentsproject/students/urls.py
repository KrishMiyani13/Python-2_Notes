from django.urls import path
from students.views import home,signup,user_login,user_logout
from students.views import add_student,view_student,update_student,delete_student,courses

urlpatterns = [

    path('', home, name='home'),
    path('signup/',signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('add_student/', add_student, name='add_student'),
    path('view_student/', view_student, name='view_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('courses/',courses, name='courses'),
]
