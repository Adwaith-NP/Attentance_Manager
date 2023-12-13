from django.contrib import admin
from Manegar.models import subjectData,subjectStudentData,attendanceDate,attendance

# Register your models here.

admin.site.register(subjectData)
admin.site.register(subjectStudentData)
admin.site.register(attendanceDate)
admin.site.register(attendance)
