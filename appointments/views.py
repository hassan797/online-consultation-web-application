import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import django.http
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template.context_processors import csrf

from .forms import *
from .models import Doctor, Patient, Appointment
import datetime
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




def BookAppointment(request, dr_id) :

    form = Appointmentform()
    doctor = Doctor.objects.get(pk=dr_id)
    drname = "Dr." + doctor.firstname+ " "+ doctor.lastname
    if request.method =='POST':

        userid = request.session.get('id')
        print(userid)
        doctor_id = dr_id

        date1 = request.POST.get('date').split("-")
        date = datetime.date(year= int(date1[0]), month= int(date1[1]),day=int(date1[2]))
        time1 = request.POST.get('time').split(":")
        time = datetime.time( int(time1[0]), int(time1[1]) )

        print(" Date requested :", date,time)
        description = request.POST.get('description')
        doctor = Doctor.objects.get( pk = doctor_id)
        patient= Patient.objects.get(user_id = userid)

        if time_isavailable(request, date, time, doctor_id):
            apointment = Appointment.objects.create( patient = patient,
                                                    doctor= doctor,
                                                    patientname = patient.firstname +" " +patient.lastname,
                                                    doctorname = "Dr. "+doctor.firstname +" " +doctor.lastname,
                                                    date = date,
                                                    time = time,
                                                    description= description )
            apointment.save()
            return HttpResponse("<h1> Your appointment has been succesfully booked :) !</h1>")
        else :
            return HttpResponse("<h1> this time slot at that day is not available :( !</h1>")

    return render(request, 'Bookappointment.html', {'form': form, 'drname': drname})


def doctorAppointments(request):

    # doctorID = request.session.get('id')
    # doctor =  Doctor.objects.get(user_id = doctorID)
    # print("INFO here :" , doctor.firstname, doctor.lastname, doctor.mobile)

    if request.method== 'POST':

        if request.POST.get("action")== "confirm":
            confirmAppointment(request)

        elif request.POST.get("action")== "Cancel":                                  # if action is cancel
            cancelappointment(request)
            
    # date__gte=datetime.today()
    appointments = Appointment.objects.filter(doctor_id= 3, ).order_by('date')
    print(len(appointments))
    return render(request , 'Appointments.html' ,{'appointments' : appointments})


# Patient :  username = jana , pass = jana1234
def patientAppointments( request):

    # userID = request.session.get('id')
    # patient =  Patient.objects.get(user_id = userID)
    # print("INFO here :" , patient.firstname, patient.lastname, patient.mobile)
    appointments = Appointment.objects.filter(patient_id = 1 , canceled = False ).order_by('date')
    return render(request , 'Appointments.html' ,{'appointments' : appointments})


def confirmAppointment(request) :

    doctorID = request.session['id']
    # doctorID = 1
    appointmentid = request.POST.get('appid')
    appointment = Appointment.objects.get(pk = appointmentid)
    appointment.confirmed = True
    appointment.save()
    print("Appointment confirmed !")


def cancelappointment(request):

    # userid = request.session.get("userid")
    # appid = request.POST.get("appid")
    userid = 1
    appid = request.POST.get("appid")
    appointment = Appointment.objects.get(pk=appid)
    appointment.canceled = True
    appointment.save()


def time_isavailable(request, date, time, doctorid):

    if not (11 < time.hour < 21):
        return False
    appts = Appointment.objects.filter(doctor_id=doctorid, date=date).order_by('time')
    print("appointments of doctor on %s : " % (str(date)), appts)
    if len(appts) == 0:
        return True
    else:
        for appointment in appts:
            time2 = appointment.time
            x = datetime.timedelta(hours=time2.hour, minutes=time2.minute, seconds=0)
            y = datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=0, )
            t3 = y - x
            delta_minutes = abs(t3.total_seconds() / 60)
            if delta_minutes >= 60:
                continue
            elif delta_minutes < 60:
                return False
        return True


def read_template(filename):

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)




def send_reminder(patient_userid, appointment) :

    doctor = appointment.doctorname
    date = appointment.date + " "+ appointment.time
    name = appointment.patientname
    email = User.objects.get(pk= patient_userid).email

    pswrd = 'your_password'

    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login('hzc01@mail.aub.edu', pswrd )
    message_template = read_template('mymessage.txt')

    # for name, email in zip(names, emails):
    msg = MIMEMultipart()  # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name, DATE = date, DOCTOR = doctor )

    # setup the parameters of the message
    msg['From'] = 'hzc01@mail.aub.edu'
    msg['To'] = email
    msg['Subject'] = 'E-health Care'

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg