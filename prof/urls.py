from django.conf.urls import url

from . import views

app_name='prof'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/home/$', views.userhome, name='user-home'),
    url(r'^user/home/company=(?P<company>.+)/run=(?P<run>[0-9]+)/', views.runhome, name='runhome')
]