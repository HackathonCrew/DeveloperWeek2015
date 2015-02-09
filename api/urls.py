from django.conf.urls import patterns, url, include
from api import views
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^get_statement$', views.returnStatement),
    url(r'^get_party_array$', views.returnPartyArray),
    url(r'^relatedstatements$', views.returnRelatedStatements),
)
