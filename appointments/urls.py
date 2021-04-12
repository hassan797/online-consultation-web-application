from django.urls import path, include
from django.conf.urls import url
from .views import ViewAppointments, ViewCalendar

urlpatterns = [
    path('', ViewAppointments),
    path("appointment/", ViewAppointments),
    path("calendar/<int:_id>", ViewCalendar),

]