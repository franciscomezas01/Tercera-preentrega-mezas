from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")

def Tipodecafe(request):
    lista = TipoDeCafe.objects.all()
    return render(request, "Tipos.html", {"Tipos": lista})

def origen(request):
    lista = Origen.objects.all()
    return render(request, "origen.html", {"origen": lista})

def preparacion(request):
    lista = Preparacion.objects.all()
    return render(request, "preparacion.html", {"preparacion": lista})

def tipodecafe_formulario(request):
    if request.method == 'POST':
        mi_formulario = TipoDeCafe_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            tipos = TipoDeCafe(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], sabor=request.POST['sabor'])
            tipos.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = TipoDeCafe_Formulario()
        return render(request, "tipo_formulario.html", {"mi_formulario": mi_formulario})
    
def origen_Formulario(request):
    if request.method == 'POST':
        mi_formulario = Origen_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            origen = Origen(nombre=request.POST['nombre'], region=request.POST['region'], pais=request.POST['pais'])
            origen.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Origen_Formulario()
        return render(request, "origen_formulario.html", {"mi_formulario": mi_formulario})
    
def Preparacion_formulario(request):
    if request.method == 'POST':
        mi_formulario = Preparacion_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            preparacion = Preparacion(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
            preparacion.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Preparacion_Formulario()
        return render(request, "preparacion_formulario.html", {"mi_formulario": mi_formulario})

def busqueda_tipo(request):
    return render(request, "busqueda_tipo.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        descripcion = TipoDeCafe.objects.filter(nombre=nombre)
        return render(request, "resultados_busqueda.html", {"nombre": nombre, "descripcion": descripcion})
    else:
        return HttpResponse("No enviaste info, por favor ingresa algo nuevamente")