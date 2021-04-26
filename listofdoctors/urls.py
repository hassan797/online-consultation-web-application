from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('listofdoctors', views.listdoctors),
    url(r'listofpatients$',views.listpatients),
    url(r'listofpatients/submit/',views.getPatients),
     path(r'listofpatients/view/<str:user>/',views.viewPatient),

]