import sqlite3 as sql
#-------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
#-------------------------------------
# Create your views here.
def instrucciones(self):
    miHtml = open("C:/Users/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/templates/template_familiares.html")
    templ_instrucciones = Template(miHtml.read())
    miHtml.close()
    miContext = Context()
    textDoc = templ_instrucciones.render(miContext)
    return HttpResponse(textDoc)