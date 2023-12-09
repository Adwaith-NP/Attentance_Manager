from django.shortcuts import render,HttpResponse,redirect
from .models import subjectData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    return render(request,'teacher_index.html')

@login_required
def addData(request):
    if request.method == 'POST':
        subject_name = request.POST['subjectName']
        subject_code = request.POST['subjectCode']
        if subjectData.objects.filter(batchCode=subject_code).exists():
            messages.warning(request,'Subject code alredy created')
            return redirect('manager:addData')
        else:
            user = request.user
            data = subjectData(subjectName = subject_name,batchCode = subject_code,user = user)
            data.save()
            return redirect('manager:teacher')
    return render(request,'addData.html')