from django.urls import path
from employee.views import home,employeeinfo,update_employee,delete_employee
urlpatterns = [
    path('',home),
    path('employeeinfo/<int:id>/',employeeinfo),
    path('update_employee/<int:id>/',update_employee),
    path('delete_employee/<int:id>/',delete_employee)
]