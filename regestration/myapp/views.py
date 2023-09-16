from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import data
from django.contrib.auth.models import auth

# Create your views here.
def reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        obj=data.objects.create(name=name,age=age,email=email,password=password)
        if password==confirm_password:
          obj.save()
          return redirect('login')
        else:
            return HttpResponse("invalid credentials")
    else:
        return render(request,'one.html')
    
def log(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')

        obj=data.objects.get(name=name,password=password)
        if (obj is not None):
          return redirect('home')
    else:
       return render(request,'login.html')
    
def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


