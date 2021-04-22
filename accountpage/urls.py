from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('account/', views.getUser), #isdoctor=1 =>Doctor; =0 =>Patient
    path('delete/', views.deleteUser),
]