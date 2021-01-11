from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log, logout as logut

# Create your views here.


    

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            else:

                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
                user.save();
                messages.info(request, 'user created')
                return redirect('login')
                
        else:
            messages.info(request, "password didn't match")
            return redirect('register')
        return redirect('/')
        




    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username = username, password = password)

        if user is not None:
            log(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


    else:
        return render(request, 'login.html')



def logout(request):
    logut(request)
    return redirect('/')