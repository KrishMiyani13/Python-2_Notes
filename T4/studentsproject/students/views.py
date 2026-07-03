from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import StudentForm
from .models import Student,Course

def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def user_login(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def home(request):
    return render(request, "home.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_student")
    else:   
        form = StudentForm()
    return render(request, "student/add_student.html",{'form':form})

def view_student(request):
    students = Student.objects.all()
    return render(request, "student/view_student.html", {'students': students})

def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    else:
        form = StudentForm(instance=student)
    return render(request, "student/update_student.html", {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_student')

def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {'courses': courses})

class CourseListCreateAPIView(generics.ListCreateAPIview):
    