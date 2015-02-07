from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def Candidate(request):
    template = loader.get_template('client/questions.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
