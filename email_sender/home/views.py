from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
 

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
        settings.EMAIL_HOST_USER,
        ['prithyanipd@rknec.edu'],
        )
   
        return render(request,"index.html",{'name':name})    
    #messages.success(request, 'Your request was sent.')
    return render(request,'index.html')
