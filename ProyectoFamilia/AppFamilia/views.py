import sqlite3 as sql
#-------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
#-------------------------------------
# Create your views here.
def instrucciones(self):
    miHtml = open("C:/Users/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/Templates/template_002.html")
    templ_instrucciones = Template(miHtml.read())
    miHtml.close()
    miContext = Context()
    textDoc = templ_instrucciones.render(miContext)
    return HttpResponse(textDoc)

def ingresoFamiliar(self,texto):
    texto = texto.replace("__"," ") # <-- hacemos que los guiones bajos los transforme en espacios
    lista = texto.split(",") # <-- generamos la lista con los campos
    # ahora separo todos los diferentes campos:
    nombre = texto[0].title()
    apellido = texto[1].title()
    fecha_nacimiento = texto[2]
    nro_documento = texto[3]