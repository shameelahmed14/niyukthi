"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('signin/',views.signin, name='signin'),
    path('feedback/',views.feedback, name='feedback'),
    path('subscribe/',views.subscribe, name='subscribe'),
    path('appointment/<phone>/',views.appointment, name='appointment'),
    path('reset/',views.reset, name='reset'),
    path('postReset/',views.postReset, name='postReset'),
    path('sendOTP/<phone>',views.sendOTP, name='sendOTP'),
    path('PasswordRest/<phone>',views.PasswordRest, name='PasswordRest'),
    path('signup/',views.signup, name='signup'),
    path('newIndex/',views.newIndex, name='newIndex'),
    path('logout/',views.logout, name='logout'),
    path('appointPatient/',views.appointPatient, name='appointPatient'),
    path('backToHome/<Phone>/',views.backToHome, name='backToHome'),
    path('myAppointment/<phone>/', views.myAppointment, name='myAppointment'),
    # path('sendAppointmentSMS/<phone>/', views.sendAppointmentSMS, name='sendAppointmentSMS'),
    
]
