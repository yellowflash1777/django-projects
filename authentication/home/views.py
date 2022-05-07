from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login

#prash19 is password

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(1,2,username,password)
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request,user)
            return redirect('/')
               # A backend authenticated the credentials
        else:
                   # No backend authenticated the credentials
                       return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')