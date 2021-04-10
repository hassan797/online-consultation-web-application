from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from .forms import *
from .models import *
from datetime import datetime
from django.utils import timezone
# Create your views here.



def ViewAppointments( request):

    form1 = Appointmentform()
    users = User.objects.all()
    if request.method== 'POST':
        pass

    return render(request , 'Appointments.html' ,{'users' : users })
