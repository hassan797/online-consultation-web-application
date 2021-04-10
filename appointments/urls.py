from django.urls import path, include
from django.conf.urls import url
import  views


urlpatterns = [
    path('', views.ViewAppointments),
    path("appointment/", views.ViewAppointments),

]