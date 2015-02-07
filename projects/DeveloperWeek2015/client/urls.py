from django.conf.urls import patterns, url, include
from github import views
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^$', views.Candidate, name='Candidate'),
)