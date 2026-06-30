from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def home(request):
    return render(request,'home.html')
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('login')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
