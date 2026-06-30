from django.shortcuts import render,redirect
from .models import Course
from .forms import Courseform

# Create your views here.
def home(requests):
    courses = Course.objects.all()
    return render(requests,'home.html',{'courses':courses})

def course_details(requests,id):
    courses = Course.objects.get(id=id)
    return render(requests,'course_details.html',{'courses':courses})

def course_add(request):
    if request.method == 'POST':
        form = Courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Courseform()

    return render(request, 'course_add.html', {'form': form})

def course_update(request,id):
    course = Course.objects.get(id=id)

    if request.method == 'POST':
        form = Courseform(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Courseform(instance=course)
    
    return render(request, 'course_update.html', {'form': form})

def course_delete(request,id):
    course = Course.objects.get(id=id)
    course.delete() 
    return redirect('/')
