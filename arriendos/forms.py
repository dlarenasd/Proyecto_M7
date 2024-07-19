from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django_select2.forms import ModelSelect2Widget
from .models import Contacto, Solicitud, Usuario, Inmueble, Comuna, Region
from django import forms

class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields = ['email', 'nombre_usuario', 'mensaje']

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['usuario', 'inmueble', 'mensaje']
        
class UsuarioForm(forms.ModelForm):
    direccion = forms.CharField(label='Dirección', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=100)
    """first_name = forms.CharField(label='Nombre', max_length=100)
    last_name = forms.CharField(label='Apellido', max_length=100)
    username = forms.CharField(label='Nombre de Usuario', max_length=100)
    email = forms.EmailField(label = 'Correo Electrónico')"""
    class Meta:
        model=Usuario
        fields = ['direccion', 'telefono']
        
    
class RegionWidget(ModelSelect2Widget):
    search_fields= [
        "nombre__icontains",
    ]
    
class ComunaWidget(ModelSelect2Widget):
    search_fields = [
        "nombre__icontains",
    ]
    
class TipoInmuebleWidget(ModelSelect2Widget):
    search_fields = [
        "nombre__icontains",
    ]

class InmuebleForm(forms.ModelForm):
    class Meta:
        model= Inmueble
        fields= ['nombre', 'descripcion', 'm2_construidos', 'm2_terreno', 'estacionamientos', 'habitaciones','banios', 'direccion','comuna', 'region', 'tipo_inmueble','precio_mensual', 'arrendada']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':15}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'rows':1, 'cols':15}),
            'region':RegionWidget(attrs={'style' : 'width:200px'}),
            'comuna': ComunaWidget(attrs={'style' : 'width:200px'}),
            'tipo_inmueble': TipoInmuebleWidget(attrs={'style' : 'width:200px'}),
            'arrendada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }