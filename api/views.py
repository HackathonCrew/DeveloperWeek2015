from django.shortcuts import render
import json
from django.http import HttpResponse
from integrate_api import getStatement, getPartyArray, getStatementMore
from idol import findRelatedStatements, getRandomIdolPerson

# Create your views here.

def returnStatement(request):
    return HttpResponse(json.dumps(getRandomIdolPerson()))

def returnPartyArray(request):
    return HttpResponse(getPartyArray())
    
def returnRelatedStatements(request):
    fullname = request.GET.get('fullname')
    
    return HttpResponse(findRelatedStatements(fullname))