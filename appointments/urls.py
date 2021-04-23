from django.urls import path, include
from django.conf.urls import url
from . import views
# from .views import ViewAppointments, ViewCalendar

urlpatterns = [
    path('', views.doctorAppointments),
    path("booksystem/<int:dr_id>", views.BookAppointment),
    path("confirm/<int:appointmentid>", views.confirmAppointment),
    path("cancel/<int:appointmentid>",  views.cancelappointment),
    # path("calendar/<int:doctorid>",views.BookAppointment ),

]