from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect #much better than return index(request) since No paramter collision
from .forms import DoctorFilter
from .models import Doctor, Patient


# Create your views here.
def listdoctors(request): #get all data from dbs
	doctors= Doctor.objects.order_by('lastname') #Organization.objects.all()

	if request.method == 'GET': #Filter
		doctorsFilter= DoctorFilter(request.GET, queryset=doctors)
		doctors= doctorsFilter.qs
	else:
		doctorsFilter= DoctorFilter()
	return render(request, 'doctors_list.html', {'doctors':doctors, 'doctorsFilter':doctorsFilter, 'user_type': 1, 'getPatient':{}})

def listpatients(request):
	print("list patients")
	if(request.method == 'GET'):
		return render(request, 'doctors_list.html', {'patient':{}, 'user_type': 0, 'getPatient':{}})

def getPatients(request):
	print("get patients: ", request.GET['patient_name'])
	patients = Patient.objects.filter(firstname=request.GET['patient_name'])
	print(patients)
	if(request.method == 'GET'):
		request.session['lastsearch'] = request.GET['patient_name']
		return render(request, 'doctors_list.html', {'patient':patients, 'user_type': 0, 'getPatient':{}})

def viewPatient(request, user):

	print("view patients: ", user)
	allPatients = Patient.objects.filter(firstname=request.session['lastsearch'])

	p = User.objects.get(username=user)
	patients = Patient.objects.filter(user=p)

	if(request.method == 'GET'):
		
		print("View patient: ", patients[0])
		return render(request, 'doctors_list.html', {'patient':allPatients, 'user_type': 0, 'getPatient':patients[0]})
