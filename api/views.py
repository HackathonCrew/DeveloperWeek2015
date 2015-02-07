from django.shortcuts import render
import json
from django.http import HttpResponse
from integrate_api import getStatement, getPartyArray

# Create your views here.

def returnStatement(request):
    return HttpResponse(getStatement())

def returnPartyArray(request):
    return HttpResponse(getPartyArray())