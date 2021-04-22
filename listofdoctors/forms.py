from django import forms
from .models import *
import django_filters 


class DoctorFilter(django_filters.FilterSet):
	class Meta:
		model = Doctor	
		fields = ['department']

