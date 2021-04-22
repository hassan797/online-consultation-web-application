from django.shortcuts import render

from django.shortcuts import redirect #much better than return index(request) since No paramter collision
from .forms import DoctorFilter
from .models import Doctor


# Create your views here.
def listdoctors(request): #get all data from dbs
	doctors= Doctor.objects.order_by('lastname') #Organization.objects.all()

	if request.method == 'GET': #Filter
		doctorsFilter= DoctorFilter(request.GET, queryset=doctors)
		doctors= doctorsFilter.qs
	else:
		doctorsFilter= DoctorFilter()
	return render(request, 'doctors_list.html', {'doctors':doctors, 'doctorsFilter':doctorsFilter})

