from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import loginData
# Register your models here.

class CustumAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_teacher', 'is_student',
        )
    
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields',{'fields': ('is_teacher', 'is_student')}),
    )
    

    
admin.site.register(loginData,CustumAdmin)