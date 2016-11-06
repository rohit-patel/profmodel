from django.conf.urls import url

from . import views

app_name='prof'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/home/$', views.userhome, name='user-home'),
    url(r'^user/home/runid-(?P<runpk>.+)/', views.runhome, name='runhome')
]