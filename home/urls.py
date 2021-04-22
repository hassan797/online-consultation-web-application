from django.conf.urls import url
#from django.conf.urls import url
from . import views

#MUST HAVE SAME NAME AS HTML TEMPLATES
urlpatterns = [
    url(r'^$', views.HomePage , name= 'homepage' ),
    url(r'^login',views.login),
    url(r'^register', views.register),
    url(r'^logout', views.logout),
    # url(r'^logout',views.logout),

]
