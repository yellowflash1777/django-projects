from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name='home'),
    path("about", views.about ,name='about'),
    path("service", views.service ,name='service'),
    path("contact", views.contact ,name='contact'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('signup',views.signupUser,name='signup'),
    path('login2',views.login2,name='login2')
]
