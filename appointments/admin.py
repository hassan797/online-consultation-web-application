from django.contrib import admin
from .models import Doctor,Patient,Appointment

# Register your models here.
# to activate virtual environment 
# Set-ExecutionPolicy Unrestricted -Scope Process

class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)
