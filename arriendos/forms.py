from django.contrib.auth.models import User
from .models import Contacto, Solicitud
from django import forms

class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields = ['email', 'nombre_usuario', 'mensaje']

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['usuario', 'inmueble', 'mensaje']
        

