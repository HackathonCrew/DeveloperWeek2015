from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.

def returnStatement(request):
    return HttpResponse(getStatement())

def getPartyArray():
    parties = [
        'republican',
        'democrat'
    ]

    return parties