from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path("",views.conveter,name="conveter"),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
    path('add_data/',views.addSubjectData,name = 'addData'),
    path('subjectDataEdit/<str:subCode>/<str:batchCode>/',views.subjectDataSection,name='subjectDataEdit'),
    path('studentAddToSub/<str:subCode>/<str:batchCode>/',views.studentAddToSub,name="studentAddToSub"),
    path('attendence_edit/<str:subCode>/<str:index>/',views.attendance_edit,name='attendance_edit'),
]