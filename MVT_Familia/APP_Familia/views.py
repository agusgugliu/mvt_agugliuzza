from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Familia.models import Persona
# -----------------------------------------
# Create your views here.
def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('APP_Familia/index.html')
    context = {
        'personas':personas,
    }
    return HttpResponse(template.render(context,request))