from django.shortcuts import render,redirect
# from django.views.generic.edit import CreateView
# from . form import addUserData
from User.models import loginData
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Manegar.models import subjectData
from django.contrib.auth.hashers import make_password
# Create your views here.

@login_required
def register(request):
    try:
        subject_data = subjectData.objects.filter(username = request.user)
        batch_list = [value.batchCode for value in subject_data]
        sorted_list = sorted(set(batch_list))
        print(sorted_list)
    except :
        subject_data = None
    if request.user.is_teacher :
        # form = addUserData(request.POST,user=request.user)
        if request.method == 'POST':
            username = request.POST['username']
            name = request.POST['name']
            batchID = request.POST['batchID']
            password = request.POST['password']
            hashed_password = make_password(password)
            if loginData.objects.filter(username = username).exists():
                messages.warning(request, "Username Taken")
            else:
                student = loginData(username = username,first_name = name,password = hashed_password,teacher_id = request.user.username,batch_id=batchID)
                student.save()
                messages.success(request, "Username added")
                return redirect('UserApp:register')
        # if form.is_valid():
        #     form.save()
        #     return redirect('login')
    else:
        return redirect('login')
    return render(request,'register.html',{'batchID':sorted_list})
