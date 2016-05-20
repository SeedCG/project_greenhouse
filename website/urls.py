from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^latest/$', views.latest, name='latest'),
]