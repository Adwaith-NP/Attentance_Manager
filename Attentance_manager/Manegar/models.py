from django.db import models
from User.models import loginData
# from django.contrib.auth.models import User

# Create your models here.

class subjectData(models.Model):
    username = models.ForeignKey(loginData,on_delete=models.CASCADE,default=1)
    subjectName = models.CharField(max_length=50)
    batchCode = models.CharField(max_length=20)
    subjectCode = models.CharField(max_length=20)
    
    def __str__(self):
        return self.subjectName

class subjectStudentData(models.Model):
    subjectCode = models.ForeignKey(subjectData,on_delete=models.CASCADE)
    studentId = models.CharField(max_length=30)
    def __str__(self):
        return self.studentId
    
class attendanceDate(models.Model):
    subjectCode = models.ForeignKey(subjectData,on_delete=models.CASCADE)
    attendanceDate = models.DateField()
    def __str__(self):
        return str(self.subjectCode)
    
class attendance(models.Model):
    attendanceDate = models.ForeignKey(attendanceDate,on_delete=models.CASCADE)
    studentId = models.CharField(max_length=30)
    attendance = models.BooleanField(default=False)
    def __str__(self):
        return str(self.studentId)
    