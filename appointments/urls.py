from django.urls import path, include
from django.conf.urls import url
from . import views
# from .views import ViewAppointments, ViewCalendar

urlpatterns = [
    path('', views.ViewAppointments),
    path("booksystem/<int:doctorid>", views.BookAppointment),
    path("booksystem/", views.BookAppointment, name = 'booker')
    # path("calendar/<int:doctorid>",views.BookAppointment ),

]