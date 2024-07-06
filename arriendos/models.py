from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

class Region(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    numeroRomano = models.CharField(max_length=25, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False, blank=False, related_name='regiones')
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False, related_name='comunas')

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=50, null=False, blank=False)
    depto = models.CharField(max_length=50, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, null=False, blank=False, related_name='direcciones',  on_delete=models.CASCADE)
    indicaciones = models.TextField(null=True, blank=True)
    
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key=True)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.ForeignKey(TipoUsuario, null=False, blank=False, related_name='usuarios',  on_delete=models.CASCADE)

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_terreno = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banios = models.IntegerField()
    direccion = models.OneToOneField(Direccion, unique=True, null=False, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, null=False, blank=False, related_name='inmuebles',  on_delete=models.CASCADE)
    precio_mensual = models.IntegerField(null=False, blank=False)
    #arrendador = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    #arrendatario = models.OneToOneField(Usuario, null=True, blank=True,  on_delete=models.CASCADE)
    arrendada = models.BooleanField(default=False)
    usuarios = models.ManyToManyField(Usuario, related_name='inmuebles')

""" 
class Solicitud(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(Usuario, null=False, blank=False)
    inmueble = models.OneToOneField(Inmueble, null=False, blank=False)
    mensaje = models.TextField(null=False, default='¡Estoy interesado!')

class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = ['fecha', 'usuario', 'inmueble', 'mensaje']
"""

