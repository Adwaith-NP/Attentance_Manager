from django.urls import path
from . import views

app_name = 'student_App'

urlpatterns = [
    path(" ",views.student,name = 'student')
]