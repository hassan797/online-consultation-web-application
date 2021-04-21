from django.shortcuts import render

from django.shortcuts import redirect #much better than return index(request) since No paramter collision
from .forms import PatientForm, DoctorForm
from .models import Doctor, Patient
from django.contrib.auth.models import User
# Create your views here.

def getUser(request, _id, isdoctor): #Get user page with info to edit
	print("Getting user maybe")
	try: #avoid invalid id error
		if (isdoctor==1):
			p = User.objects.get(id=_id)
			user = Doctor.objects.get(user=p)
			form = DoctorForm(instance=user)
		elif (isdoctor==0):

			p = User.objects.get(id=_id)
			user = Patient.objects.get(user=p)
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
				return render(request, 'account.html', {'form': form, 'id':_id, 'isdoctor':isdoctor } ) #NOTE: VARIABLES IN HTML CANNOT START WITH '_' SO NO "_id"

		else: # See User data. Logically renders first since first accessed thorugh GET
			return render(request, 'account.html', {'form': form, 'id':_id, 'isdoctor':isdoctor } )
	except:
		return redirect('/')

def deleteUser(request, _id, isdoctor): #API that renders back index
	try: #avoid invalid id error
		if isdoctor==1:
			user = Doctor.objects.get(id=_id)
		elif isdoctor==0:
			user = Patient.objects.get(id=_id)
		else:
			return redirect('/')
		user.delete()
	except:
		pass

	return redirect('/')
