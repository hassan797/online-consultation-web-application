from django.conf.urls import url
#from django.conf.urls import url
from . import views

#MUST HAVE SAME NAME AS HTML TEMPLATES
urlpatterns = [
    url(r'^$', views.HomePage),
    url(r'^Login',views.login),
    url(r'^Signup', views.register),
    #     url(r'^logout',views.logout),

]
