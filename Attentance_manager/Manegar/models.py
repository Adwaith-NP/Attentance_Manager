from django.db import models
from User.models import loginData
# from django.contrib.auth.models import User

# Create your models here.

class subjectData(models.Model):
    user = models.ForeignKey(loginData,on_delete=models.CASCADE,default=1)
    subjectName = models.CharField(max_length=50)
    batchCode = models.CharField(max_length=20)
    subjectCode = models.CharField(max_length=20)
    
    def __str__(self):
        return self.subjectName

class subjectStudentData(models.Model):
    subjectCode = models.ForeignKey(subjectData,on_delete=models.CASCADE)
    studentId = models.CharField(max_length=30)
    attendanceDate = models.DateField()
    