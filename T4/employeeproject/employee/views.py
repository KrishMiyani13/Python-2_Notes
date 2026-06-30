from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()

    name = request.POST.get('name')
    id = request.POST.get('id')
    email = request.POST.get('email')
    department = request.POST.get('department')
    designation = request.POST.get('designation')
    salary = request.POST.get('salary')

    if name:
        employees = employees.filter(name__icontains= name)

    return render(request,'home.html',{'employees': employees})

def employeeinfo(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,"employeeinfo.html",{'employee':employee})

def update_employee(request,id):
    employee = Employee.objects.get(id=id)
    
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.id = request.POST.get('id')
        employee.email = request.POST.get('email')
        employee.department = request.POST.get('department')
        employee.designation = request.POST.get('designation')
        employee.salary = request.POST.get('salary')
        employee.save()

        return redirect('/')

    return render(request,'update_employee.html',{'employee':employee})


def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect('/')