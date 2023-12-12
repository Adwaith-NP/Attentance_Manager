from django.shortcuts import render,redirect
# from django.views.generic.edit import CreateView
# from . form import addUserData
from User.models import loginData
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Manegar.models import subjectData
# Create your views here.

@login_required
def register(request):
    try:
        subject_data = subjectData.objects.filter(teacher_id = request.user)
    except subject_data.DoesNotExist:
        subject_data = None
    if request.user.is_teacher :
        # form = addUserData(request.POST,user=request.user)
        if request.method == 'POST':
            username = request.POST['username']
            name = request.POST['name']
            batchID = request.POST['batchID']
            password = request.POST['password']
            if loginData.objects.filter(username = username).exists():
                messages.warning(request, "Username Taken")
            else:
                student = loginData(username = username,first_name = name,password = password,teacher_id = request.user.username,batch_id=batchID)
                student.save()
                messages.success(request, "Username added")
                return redirect('UserApp:register')
        # if form.is_valid():
        #     form.save()
        #     return redirect('login')
    else:
        return redirect('login')
    return render(request,'register.html',{'batchID':subject_data})
