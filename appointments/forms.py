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
        fields = ['address', 'mobile', 'department', 'status']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['address', 'mobile', 'status', 'chronic_deseases', 'unimmune_to']


# class book(forms.ModelForm):
#     # appointment_date= DateTimeField(widget = DateInput(format='%Y-%m-%d'),
#     #                                   input_formats=('%Y-%m-%d',),
#     #                                   required=False)
#     class Meta:
#         model = Appointment1
#         fields = ("name", "contact_no", "specialist", "date")
#         widgets = {
#             'date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
#         }

class Appointmentform(forms.ModelForm):
    # appointment_date= DateTimeField(widget = DateInput(format='%Y-%m-%d'),
    #                                   input_formats=('%Y-%m-%d',),
    #                                   required=False)
    # doctorId = forms.ModelChoiceField(queryset= Doctor.objects.all().filter(status=True),
                                      # to_field_name="firstname")

    # patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True), to_field_name="user_id")
    class Meta:
        model = Appointment
        fields = [  'doctorname', 'date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd', 'type':'date'}),
            'time' : forms.TimeInput(attrs={'type' : 'time'})
        }
