from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi pagina de django</h1>')

def inicio(request):
    template = loader.get_template('inicio.html')

    datos = {
        'lista' : ['primero', 'segundo', 'tercero'],
        'nombre' : 'Juancho',
        'apellido' : 'Ford',
    }

    plantilla_generada = template.render(datos)

    return HttpResponse(plantilla_generada)