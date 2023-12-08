# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import loginData

# class addUserData(UserCreationForm):
#     class Meta:
#         model = loginData
#         fields = ['username', 'first_name', 'last_name','password1','password2','teacher_id']
#         widgets = {
#             'teacher_id': forms.HiddenInput(),
#         }
        
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super(addUserData, self).__init__(*args, **kwargs)
#         if user and user.is_authenticated and user.is_teacher:
#             self.fields['teacher_id'].initial = user.username
