from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method=='POST':
        rusername=request.POST.get('name')
        rmail=request.POST.get('email')
        rpassword=request.POST.get('password')
        rconfirmpassword=request.POST.get('confirmpassword')
        if rpassword!=rconfirmpassword:
            return HttpResponse["Password and ConfirmPassword are not Matching"]
        else:
            user_registration=User.objects.create_user(rusername,rmail,rpassword)
            user_registration.save()
            return redirect(login1)   
    return render(request,"registration.html")
def login1(request):
    if request.method=='POST':
        rusername=request.POST.get('name')
        rpassword=request.POST.get('password')
        user=authenticate(request,username=rusername,password=rpassword)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            return HttpResponse('Invalid password')
    return render(request,'login.html')    
@login_required(login_url='log')
def home(request):
    return render(request,'home.html')
def logout1(request):
    logout(request)
    return redirect(login1)
