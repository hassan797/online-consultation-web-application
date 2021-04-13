from django.conf.urls import url
#from django.conf.urls import url
from . import views

#MUST HAVE SAME NAME AS HTML TEMPLATES
urlpatterns = [
    url(r'^$',views.index),
    url(r'^login', views.login),
    url(r'^register', views.register, name = "home-register"),
#     url(r'^logout',views.logout),
    url(r'^HomePage', views.HomePage, name = "home"),
   

]
