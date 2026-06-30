from django.urls import path
from .views import home,course_details,course_add,course_update,course_delete
urlpatterns = [
    path('',home,name='home'),
    path('course_details/<int:id>',course_details),
    path('add/',course_add),
    path('update/<int:id>',course_update),
    path('delete/<int:id>',course_delete),

]