from django.shortcuts import render

# Create your views here.
# Home 
def home(request):
    return render (request,"home.html")

#About
def about(request):
    name = "Krish"
    std_id = [1,2,3,4,5]
    std_name = ['A','B','C','D','E']
    data = {
        "std_id":std_id,
        "std_name":std_name
    }
    data1 = {'course_name' : 'python',"durstion":'2','fees':2000,'result':90}

    return render (request,"about.html",{"data":data1})

#course
def course(request):
    return render (request,"course.html")

