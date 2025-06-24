from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py
from ordenamiento.forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def listar_parroquia(request):
    # Listar los registros del modelo Estudiante, obtenidos de la base de datos.
    parroquias = Parroquia.objects.all()
    # Listar los registros del modelo Estudiante, obtenidos de la base de datos.
    barrios = Barrio.objects.all()
    # Se agregará la información que estará disponible en el template
    informacion_template = {'parroquias': parroquias, 'barrios': barrios}
    return render(request, 'listar_parroquias.html', informacion_template)


def crear_parroquia(request):
    print(request)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_parroquia.html', diccionario)


def listar_barrio(request):
    # Listar los registros del modelo Estudiante, obtenidos de la base de datos.
    barrios = Barrio.objects.all()
    # Se agregará la información que estará disponible en el template
    informacion_template = {'barrios': barrios}
    return render(request, 'listar_barrios.html', informacion_template)


def crear_barrio(request):
    print(request)
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_parroquia.html', diccionario)
