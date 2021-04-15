from django.shortcuts import render

from django.shortcuts import redirect #much better than return index(request) since No paramter collision
from .forms import PatientForm, DoctorForm
from .models import Doctor, Patient

# Create your views here.

def getUser(request, _id, isdoctor): #Get user page with info to edit
	try: #avoid invalid id error
		if (isdoctor==1):
			user = Doctor.objects.get(id=_id)
			form = DoctorForm(instance=user)
		elif (isdoctor==0):
			user = Patient.objects.get(id=_id)
			form = PatientForm(instance=user)
		else:
			return redirect('/')
		# global doctorselected
		# doctorselected=False

		if request.method == 'POST': #Edit User (editUser)
			if isdoctor==1:
				form = DoctorForm(request.POST, instance=user)
			elif isdoctor==0:
				form = PatientForm(request.POST, instance=user)
			else:
				return redirect('/')
			if form.is_valid():
				form.save()
				return render(request, 'account.html', {'form': form } )

		else: # See User data. Logically renders first since first accessed thorugh GET
			return render(request, 'account.html', {'form': form } )
	except:
		return redirect('/')