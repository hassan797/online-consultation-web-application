from django.db import models




class Doctor(models.Model):

    Departments = [
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Dermatology", "Dermatology"),
        ("Cancer", "Cancer"),
        ("Psychiatric" , "Psychiatric")
    ]
    firstname =models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null= True)
    mobile = models.CharField(max_length=100,null=True)
    department= models.CharField(max_length=100, choices= Departments)

    def __str__(self):
        return "{} ({})".format(self.firstname+" "+self.lastname, self.department)



class Patient(models.Model):

    firstname =models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=40,  null= True)
    mobile = models.CharField(max_length=20,null= True)
    symptoms = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.firstname+" "+self.lastname

    
    
class Appointment(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment_doctor')
    patientName=models.CharField(max_length=40,null=True)
    doctorName =models.CharField(max_length=40,null=True)
    appointmentime = models.DateTimeField()
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=True)

    def __str__(self):
        return  '%s  with %s at %s ' % ( self.patient.__str__() , self.doctor.__str__(),self.appointmentime )

