from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__' # fields = ['firstname','lastname','address','mobile','department','zoom_link']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
