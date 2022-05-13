from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    #return HttpResponse("yoo homepage")
    messages.success(request, 'Your request was sent.')

    return render(request,'index.html')
