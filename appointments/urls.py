from django.urls import path, include
from django.conf.urls import url
from .views import ViewAppointments

urlpatterns = [
    path('', ViewAppointments),
    path("appointment/", ViewAppointments),

]