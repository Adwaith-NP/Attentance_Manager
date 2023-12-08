from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("conveter/",views.conveter,name="conveter"),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
    path('add_data/',views.addData,name = 'addData'),
]