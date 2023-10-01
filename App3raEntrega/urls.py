from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('tipo', Tipodecafe, name='tipos'),
    path('origen', origen, name='origen'),
    path('preparacion', preparacion, name='preparacion'),
    path('agregar-tipo', tipodecafe_formulario, name='Agregartipo'),
    path('agregar-origen', origen_Formulario, name='Agregarorigen'),
    path('agregar-preparacion', Preparacion_formulario, name='AgregarPreparacion'),
    path('', inicio, name='Inicio'),
    path('busq-gen', busqueda_tipo, name="BusquedaTipo"),
    path('buscar', buscar, name="Buscar"),
]