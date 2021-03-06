from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from Familia.forms import PersonaForm
from Familia.models import Persona
# -------------------------------------------------------------------------------------
def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/index.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))
# -------------------------------------------------------------------------------------
def agregar(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            documento = form.cleaned_data['documento']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, documento=documento).save()

            return HttpResponseRedirect("/familia/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'familia/form_carga.html', {'form': form})
# -------------------------------------------------------------------------------------
def borrar(request, identificador):
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
# -------------------------------------------------------------------------------------
def actualizar(request, identificador):
    pass