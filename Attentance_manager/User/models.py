from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class loginData(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    batch_id = models.CharField(max_length=30,default='None')
    teacher_id = models.CharField(max_length=30,blank=True,null=True)
