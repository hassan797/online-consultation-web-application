from django.db import models
from django.contrib.auth.models import User



class Doctor(models.Model):

    Departments = [
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Dermatology", "Dermatology"),
        ("Cancer", "Cancer"),
        ("Psychiatric" , "Psychiatric")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null= True)
    firstname =models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null= True)
    mobile = models.CharField(max_length=100,null=True)
    department= models.CharField(max_length=100, choices= Departments)
    status = models.BooleanField(default=True)
    zoom_link = models.CharField(max_length= 300, null= True)

    def __str__(self):
        return "{} ({})".format(self.firstname+" "+self.lastname, self.department)



class Patient(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE , null= True)
    firstname =models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=40,  null= True)
    mobile = models.CharField(max_length=20,null= True)
    chronic_deseases = models.CharField(max_length=100,null=True)
    unimmune_to = models.TextField(max_length=300, null= True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname+" "+self.lastname


# class PreAppointment(models.Model):
#
#     Departments = [
#         ("Cardiology", "Cardiology"),
#         ("Neurology", "Neurology"),
#         ("Dermatology", "Dermatology"),
#         ("Cancer", "Cancer"),
#         ("Psychiatric", "Psychiatric")
#     ]
#
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment_patient')
#     department = models.CharField(max_length=50, choices=Departments)


class Appointment(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment_doctor')
    patientName=models.CharField(max_length=40,null=True)
    doctorName =models.CharField(max_length=40,null=True)
    date = models.DateField(null=True)
    time = models.fields.TimeField(null=True)
    description=models.TextField(max_length=500, null=True)
    confirmed = models.BooleanField(default= False)

    def __str__(self):
        return  '%s  with %s AT %s ' % ( self.patient.__str__() , self.doctor.__str__(),str(self.time)  )



# hass = Appointment.objects.get()
# hass.delete()
# print("hassan = ")
