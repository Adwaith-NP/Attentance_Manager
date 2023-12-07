from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import loginData

class addUserData(UserCreationForm):
    class Meta:
        model = loginData
        fields = ['username', 'email', 'first_name', 'last_name',
        'is_teacher', 'is_student','password1','password2']