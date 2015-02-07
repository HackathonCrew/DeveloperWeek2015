from django.shortcuts import render

# Create your views here.
def Candidate(request):
    template = loader.get_template('client/questions.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
