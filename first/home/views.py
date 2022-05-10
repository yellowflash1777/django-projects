from cgitb import html
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    
    
    return render(request,'index.html')
    #return HttpResponse("yoo homepage")

def about(request):
    return render(request,'about.html')

   

def service(request):
    return render(request,'service.html')

   

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email = email,phone = phone ,desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your request was sent.')

    return render(request,'contact.html')

    