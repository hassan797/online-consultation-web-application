from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['address', 'mobile', 'department', 'status', 'profile_pic']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['address', 'mobile', 'status', 'chronic_deseases', 'unimmune_to']


class Appointmentform(forms.ModelForm):
    # appointment_date= DateTimeField(widget = DateInput(format='%Y-%m-%d'),
    #                                   input_formats=('%Y-%m-%d',),
    #                                   required=False)
    class Meta:
        model = Appointment
        fields = ['doctor', 'description', 'date', 'time']
        # widgets = {
        #     'date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
        # }
