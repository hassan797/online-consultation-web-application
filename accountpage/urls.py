from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('account/<int:_id>/<int:isdoctor>', views.getUser), #isdoctor=1 =>Doctor; =0 =>Patient
    path('delete/<int:_id>/<int:isdoctor>', views.deleteUser),
]