from cgitb import html
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')        
    return render(request,'index.html')
    #return HttpResponse("yoo homepage")

def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'about.html')

   

def service(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'service.html')

   

def contact(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email = email,phone = phone ,desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your request was sent.')

    return render(request,'contact.html')

def loginUser(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(1,2,username,password)
        user = authenticate(username=username, password=password)
        messages.success(request, ' Login successful    .')

        if user is not None:
            login(request,user)
            return redirect('/')
               # A backend authenticated the credentials
        else:
                   # No backend authenticated the credentials
                       return render(request,'login2.html')

    return render(request,'login2.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def signupUser(request):
    if request.method=='POST':
        fname =request.POST.get('fname')
        lname =request.POST.get('lname')
        username =request.POST.get('username')
        email =request.POST.get('email')
        password =request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request, 'Your account have been succesfully created.')
        send_mail('Welcome to Prashant\'s world',f'Hi {user.first_name}, thank you for registering in Prashant\'s Store .',settings.EMAIL_HOST_USER,[user.email],)
       # user1 = authenticate(username=username, password=password)
       
        if user is not None:
            login(request,user)
            return redirect('/')
               # A backend authenticated the credentials
        else:
                   # No backend authenticated the credentials
                       return render(request,'login2.html')
        return render(request,'login2.html')
   # if request.user.is_anonymous:
    #    return redirect('/login')
    return render(request,'signup.html')

def login2(request):
   # if request.user.is_anonymous:
    #    return redirect('/login')
    return render(request,'login.html')