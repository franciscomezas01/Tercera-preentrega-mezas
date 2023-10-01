from django import forms

class TipoDeCafe_Formulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)
    sabor = forms.CharField(max_length=200)
    
class Origen_Formulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    pais = forms.CharField(max_length=200)
    region = forms.CharField(max_length=200)
    

class Preparacion_Formulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)
    


