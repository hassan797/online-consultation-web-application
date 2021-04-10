from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context_processors import csrf
from .forms import *
from datetime import datetime
from django.utils import timezone
# Create your views here.



def ViewAppointments( request):

    form1 = Appointmentform()
    if request.method== 'POST':
        pass

    return render(request , 'Appointments.html' ,{'form' : form1})
