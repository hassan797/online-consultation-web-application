import django.http
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.context_processors import csrf
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


def BookAppointment(request, doctorID) :

    userid = request.session['user_id']
    doctor_id = doctorID
    


def ViewCalendar(request, id):

    return render(request , 'Calendar.html' ,{ })
