from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from . form import addUserData
# Create your views here.

def register(request):
    form = addUserData(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'register.html',{'form':form})
