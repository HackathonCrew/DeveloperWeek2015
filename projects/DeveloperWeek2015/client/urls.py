from django.conf.urls import patterns, url, include
from client import views
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^$', views.Candidate, name='Candidate'),
)
