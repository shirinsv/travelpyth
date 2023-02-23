from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
        if request.method=='POST':
            username=request.POST['username']
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            confirmpassword=request.POST['confirm_password_']
            if password==confirmpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email id taken")
                    return redirect('register')
                else:
                    user_=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                    user_.save()
                    return redirect('login')

            else:
                messages.info(request,"password not matching")
                return redirect('register')
            return redirect('/')
        return render(request,"register.html")