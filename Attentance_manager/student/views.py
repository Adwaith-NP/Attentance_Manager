from django.shortcuts import render
from Manegar.models import subjectData,subjectStudentData,attendanceDate,attendance
from django.db.models import Count,Q

# Create your views here.

def student(request):
    batch_id = request.user.batch_id
    subjectData_instance = subjectData.objects.filter(batchCode = batch_id)
    subjectStudentData_instance = subjectStudentData.objects.filter(subjectCode__in = subjectData_instance,studentId = request.user)
    attendanceDate_instance = attendanceDate.objects.filter(subjectCode__in = subjectData_instance)
    attendance_instance = attendance.objects.filter(
        attendanceDate__in = attendanceDate_instance,
        studentId = request.user
        ).values(
            'studentId',
            'attendanceDate__subjectCode__subjectName',
        ).annotate(
            attendance_count_total=Count('studentId'),
            attendance_count_as_present=Count('attendance', filter=Q(attendance=True))
        )
    attendanceTottalPrecentage = [0,0]
    for entry in attendance_instance:
        tottalClass = int(entry['attendance_count_total'])
        presentedClass = int(entry['attendance_count_as_present'])
        try : 
            attendencePrecentage = (presentedClass/tottalClass)*100
            entry['attendencePrecentage'] = round(attendencePrecentage,2)
            attendanceTottalPrecentage[0] = attendanceTottalPrecentage[0]+1
            attendanceTottalPrecentage[1] = attendanceTottalPrecentage[1]+entry['attendencePrecentage']
        except : 
            pass
    TottalPrecentage = 0 
    try :
        TottalPrecentage = round(((attendanceTottalPrecentage[1]/(attendanceTottalPrecentage[0]*100))*100),2)
    except :
        pass
    data = {'subjectAllData':attendance_instance,
            'TottalPrecentage' : TottalPrecentage,
            }
    
    return render(request,'student_home_page.html',data)


