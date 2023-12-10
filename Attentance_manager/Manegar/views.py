from django.shortcuts import render,HttpResponse,redirect
from .models import subjectData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from User.models import loginData
# from django.contrib.auth import get_user_model as Users

# Create your views here.
@login_required
def conveter(request):
    if request.user.is_authenticated and request.user.is_student :
        print('I am a student')
    elif request.user.is_authenticated and request.user.is_teacher :
        return redirect('manager:teacher')
        
    return HttpResponse("<H1>Error 404</H1>")

@login_required
def student(request):
    pass

@login_required
def teacher(request):
    if request.user.is_teacher :
        try:
            subject_data = subjectData.objects.filter(user = request.user)
        except subject_data.DoesNotExist:
            subject_data = None
        return render(request,'teacher_index.html',{'subject':subject_data})
    else:
        return redirect('login')
    
def subjectDataEdite(requset,subCode,batchCode):
    if requset.user.is_teacher:
        
        return render(requset,'subjectDataEdite.html')
    else:
        return redirect('login')

@login_required
def addData(request):
    if request.user.is_teacher :
        if request.method == 'POST':
            subject_name = request.POST['subjectName']
            subject_code = request.POST['subjectCode']
            batchCode = request.POST['batchCode']
            if subjectData.objects.filter(batchCode=subject_code).exists():
                messages.warning(request,'Subject code alredy created')
                return redirect('manager:addData')
            else:
                user = request.user
                data = subjectData(subjectName = subject_name,batchCode = batchCode,user = user,subjectCode = subject_code)
                data.save()
                return redirect('manager:teacher')
    else:
        return redirect('login')
    return render(request,'addData.html')