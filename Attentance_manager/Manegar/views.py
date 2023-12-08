from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth import get_user_model as Users

# Create your views here.

def conveter(request):
    # user = Users()
    if request.user.is_authenticated and request.user.is_student :
        print('I am a student')
    elif request.user.is_authenticated and request.user.is_teacher :
        return redirect('manager:teacher')
        
    return HttpResponse("<H1>Error 404</H1>")

def student(request):
    pass

def teacher(request):
    return render(request,'teacher_index.html')

def addStudent(request):
    return render(request,'addStudent.html')

def addData(request):
    return render(request,'addData.html')