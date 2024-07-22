from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.forms import forms



# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f"{self.nombre}"

class Region(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    numeroRomano = models.CharField(max_length=25, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False, blank=False, related_name='regiones')
    
    def __str__(self):
        return f"{self.numeroRomano} - {self.nombre} - {self.pais}"
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False, related_name='comunas')
    
    def __str__(self):
        return f"{self.nombre} - {self.region.nombre}, {self.region.pais}"
    
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = False)
    rut = models.CharField(max_length=12, primary_key=True)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.ForeignKey(TipoUsuario, null=False, blank=False, default=2, related_name='usuarios',  on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.rut} | {self.tipo_usuario}"

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Inmueble(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_terreno = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banios = models.IntegerField()
    direccion = models.CharField(max_length=100, null=False, blank=False)
    comuna = models.ForeignKey(Comuna, null=False, blank=False, related_name='direcciones',  on_delete=models.CASCADE)
    region = models.ForeignKey(Region, null=False, blank=False, related_name='direcciones',  on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, null=False, blank=False, related_name='inmuebles',  on_delete=models.CASCADE)
    precio_mensual = models.IntegerField(null=False, blank=False)
    arrendada = models.BooleanField(default=False)
    usuarios = models.ManyToManyField(Usuario, related_name='inmuebles')
    
    def __str__(self):
        return f"{self.nombre} - {self.direccion}, {self.comuna.nombre}"

class Contacto(models.Model):
    email = models.EmailField(null = False, blank=False)
    nombre_usuario = models.CharField(max_length=64, null=False, blank=False)
    mensaje = models.TextField(null=False, blank=False)

    
    def __str__(self):
        return f"Formulario de Contacto: {self.id} - {self.nombre_usuario}"

class Solicitud(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    inmueble = models.OneToOneField(Inmueble, null=False, blank=False, on_delete=models.CASCADE)
    mensaje = models.TextField(null=False, blank=False, default='¡Estoy interesado!')



