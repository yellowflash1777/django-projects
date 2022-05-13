from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
    #return HttpResponse("yoo homepage")
        send_mail(
        subject,
        message,
        email,
        ['prithyani2002@gmail.com'],
        )
   
        return render(request,"index.html",{'name':name})    
    #messages.success(request, 'Your request was sent.')
    return render(request,'index.html')
