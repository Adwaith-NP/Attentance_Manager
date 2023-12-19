from django.shortcuts import render,HttpResponse,redirect
from .models import subjectData,subjectStudentData,attendanceDate,attendance
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from User.models import loginData
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
# from django.contrib.auth import get_user_model as Users

# Create your views here.
@login_required
def conveter(request):
    if request.user.is_authenticated and request.user.is_student :
        return redirect('student_App:student')
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
            subject_data = subjectData.objects.filter(username = request.user)
        except subject_data.DoesNotExist:
            subject_data = None
        return render(request,'teacher_index.html',{'subject':subject_data})
    else:
        return redirect('login')
    
# The view works for showing the student details and attendes adding page 
@login_required
def subjectDataSection(request,subCode,batchCode):
    if request.user.is_teacher:
        subjectData_instance = subjectData.objects.get(subjectCode = subCode,batchCode = batchCode)
        added_student = subjectStudentData.objects.filter(subjectCode = subjectData_instance)
        
        #collecting the attendance date
        if request.method == 'POST' and 'attendanceForm' in request.POST:
            attendance_date = request.POST.get('date', None)
            print(attendance_date)
            try:
                # Attempt to parse the date string, attendance_date covert the collected date to the datetime.date function 
                attendance_date = datetime.strptime(attendance_date, '%Y-%m-%d').date()
                if attendanceDate.objects.filter(attendanceDate = attendance_date,subjectCode = subjectData_instance).exists():
                    attendanceDate_instance = attendanceDate.objects.filter(attendanceDate=attendance_date).order_by('-pk').first()
                    additional_class = attendanceDate_instance.additional
                    additional_class += 1
                    save_data = attendanceDate(subjectCode = subjectData_instance,attendanceDate = attendance_date,additional = additional_class)
                    save_data.save()
                else:
                    save_data = attendanceDate(subjectCode = subjectData_instance,attendanceDate = attendance_date)
                    save_data.save()
                return HttpResponseRedirect(request.path_info)
            except ValueError:
                print('error')
                messages.warning(request, 'Invalid date format. Please use YYYY-MM-DD.')
        
        # latest_created_date store the latest uploaded date
        try:
            latest_created_date = attendanceDate.objects.filter(subjectCode = subjectData_instance).latest('pk')
        except attendanceDate.DoesNotExist:
            latest_created_date = None
        
        #list out student ID and student Name
        student_names = []
        for student_name in added_student:
            name = loginData.objects.get(username = student_name.studentId)
            student_names.append((student_name.studentId,name.first_name))
            
        #collect the student attendance
        if request.method == 'POST' and 'attendance' in request.POST:
            presentStudentID = request.POST.getlist('student_attendance')
            for studentID,student_name in student_names:
                if attendance.objects.filter(attendanceDate = latest_created_date,studentId = studentID).exists():
                    messages.warning(request,'error')
                else:
                    if studentID in presentStudentID:
                        addAttendence = attendance(attendanceDate = latest_created_date,studentId = studentID,attendance = True)
                        addAttendence.save()
                    else:
                        addAttendence = attendance(attendanceDate = latest_created_date,studentId = studentID)
                        addAttendence.save()
            return HttpResponseRedirect(request.path_info)    
        # if the top list date is stored alrady in attendance database the latest_created_date go to None
        if latest_created_date and attendance.objects.filter(attendanceDate = latest_created_date).exists():
            latest_created_date = None
            
        # saveDate store all saved date in attendanceDate database
        savedDates = attendanceDate.objects.filter(subjectCode = subjectData_instance).order_by('-pk')
        
            
        data = {
            'subCode':subCode,
            'batchCode':batchCode,
            'added_student' : added_student,
            'student_name' : student_names,
            'new_date' : latest_created_date,
            'savedDate' : savedDates,
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
                data = subjectData(subjectName = subject_name,batchCode = batchCode,username = user,subjectCode = subject_code)
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
            added_student_list = request.POST.getlist('addedStudentList')
            subject_instance = subjectData.objects.get(subjectCode=subCode,batchCode = batchCode) # subject_instance store the instance of subjectCode for creating a foreignkey
            for student in loginData.objects.filter(batch_id = batchCode):
                if student.username in added_student_list:
                    if subjectStudentData.objects.filter(studentId = student.username,subjectCode = subject_instance).exists():
                        pass
                    else:
                        try:
                            selected_student = subjectStudentData(subjectCode = subject_instance,studentId = student.username)
                            selected_student.save()
                        except:
                            print('error')
            return redirect(reverse('manager:subjectDataEdit', args=[subCode,batchCode]))
        #collect all student data from loginData database that filter with batch_id
        subject_instance = subjectData.objects.get(subjectCode=subCode)
        studentList = loginData.objects.filter(batch_id = batchCode)
        addedStudents = subjectStudentData.objects.filter(subjectCode = subject_instance)
        added_student_ids = [student.studentId for student in addedStudents]
        filtered_student_list = studentList.exclude(username__in=added_student_ids)
        return render(request,'studentAddToSub.html',{'sudentList':filtered_student_list})
    else:
        return redirect('login')
    
def attendance_edit(request,subCode,index,):
    print(subCode,index)
    return render(request,'attendance.html') 