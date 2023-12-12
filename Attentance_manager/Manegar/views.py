from django.shortcuts import render,HttpResponse,redirect
from .models import subjectData,subjectStudentData,attendanceDate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from User.models import loginData
from django.urls import reverse
# from django.contrib.auth import get_user_model as Users

# Create your views here.
@login_required
def conveter(request):
    if request.user.is_authenticated and request.user.is_student :
        print('I am a student')
    elif request.user.is_authenticated and request.user.is_teacher :
        return redirect('manager:teacher')
        
    return HttpResponse("<H1>Error 404</H1>")

@login_required  #Create a new APP for Student
def student(request):
    pass

# Teacher page for listing added subjects and adisional  data
@login_required
def teacher(request):
    if request.user.is_teacher :
        try:
            subject_data = subjectData.objects.filter(teacher_id = request.user)
        except subject_data.DoesNotExist:
            subject_data = None
        return render(request,'teacher_index.html',{'subject':subject_data})
    else:
        return redirect('login')
    
# The view works for showing the student details and attendes adding page 
@login_required
def subjectDataSection(request,subCode,batchCode):
    if request.user.is_teacher:
        subjectData_instance = subjectData.objects.get(subjectCode = subCode)
        added_student = subjectStudentData.objects.filter(subjectCode = subjectData_instance)
        student_names = []
        for student_name in added_student:
            name = loginData.objects.get(username = student_name.studentId)
            student_names.append((student_name.studentId,name.first_name))
        data = {
            'subCode':subCode,
            'batchCode':batchCode,
            'added_student' : added_student,
            'student_name' : student_names,
            }
        return render(request,'subjectDataEdite.html',data)
    else:
        return redirect('login')

# The function for adding subjects to the data base
@login_required
def addSubjectData(request):
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
                data = subjectData(subjectName = subject_name,batchCode = batchCode,teacher_id = user,subjectCode = subject_code)
                data.save()
                return redirect('manager:teacher')
    else:
        return redirect('login')
    return render(request,'addData.html')

# The view works for removing same students form the students list if requard
@login_required
def studentAddToSub(request,subCode,batchCode):
    if request.user.is_teacher :
        if request.method == 'POST':
            #for cheking the student was remove or not and adding to the data to subjectStudentData data base
            removed_student_list = request.POST.getlist('removedStudentList')
            subject_instance = subjectData.objects.get(subjectCode=subCode) # subject_instance store the instance of subjectCode for creating a foreignkey
            for student in loginData.objects.filter(batch_id = batchCode):
                if student.username not in removed_student_list:
                    try:
                        selected_student = subjectStudentData(subjectCode = subject_instance,studentId = student.username)
                        selected_student.save()
                    except:
                        print('error')
            return redirect(reverse('manager:subjectDataEdit', args=[subCode,batchCode]))
        sudentList = loginData.objects.filter(batch_id = batchCode)
        return render(request,'studentAddToSub.html',{'sudentList':sudentList})
    else:
        return redirect('login')