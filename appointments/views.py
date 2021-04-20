import django.http
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template.context_processors import csrf

from . import  models
from .forms import *
from .models import *
from datetime import datetime
from django.utils import timezone
# Create your views here.


def signup(request):

    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("") # take user to home page
    return render(request, "appointment/register.html", {'form': form})


def loginuser(request):

    print(request.user.username)
    if request.method == "POST":
        username = request.POST.get("username")
        passwrd = request.POST.get("password")
        member = User.objects.get(username=request.POST['username'])
        if member.password== passwrd :
            request.session['user_id'] = member.id
            login(request, member)
            return HttpResponseRedirect('')
        else:
            messages.info(request, "username or password is incorect")
    return render(request, "")


def logoutuser(request):
    for i in list(request.session.keys()):
        del request.session[i]
    logout(request)
    return redirect("loginuser")


def ViewAppointments( request):

    form1 = Appointmentform()
    users = User.objects.all()
    if request.method== 'POST':
        pass

    return render(request , 'Appointments.html' ,{'users' : users })


def BookAppointment(request) :


    form = Appointmentform()
    # drfname = Doctor.objects.filter(pk=doctorid)[0].firstname
    # drlname = Doctor.objects.filter(pk=doctorid)[0].lastname
    # name = drfname + " " + drlname

    if request.method =='POST':

        userid = 1
        doctor_id = 1
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        link = Doctor.objects.filter(id = doctor_id)
        apppointment2 = Appointment(request.POST)
        apppointment2.patient= Patient.objects.filter(pk = userid)[0]
        apppointment2.doctor = Doctor.objects.filter(pk = doctor_id)[0]
        apppointment2.save()
        # apointment = models.Appointment.objects.create( patient = Patient.objects.filter(pk = userid),
        #                                                 doctor= Doctor.objects.filter(pk = doctor_id),
        #                                                 doctorname = name,
        #                                                 date = date,
        #                                                 time = time,
        #                                                 description= description )
        # apointment.save()
        return HttpResponse("<h1> Your appointment has been succesfully booked !</h1>")
    return render(request, 'Bookappointment.html', {'form': form, 'drname': 'ali assi'})
    # return HttpResponse(form)









def ViewCalendar(request, id):

    return render(request , 'Calendar.html' ,{ })
