from django.contrib import admin
from .models import Pais, Region, Comuna, Direccion, Inmueble, TipoInmueble, Usuario, TipoUsuario
# Register your models here.
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Inmueble)
admin.site.register(TipoInmueble)
admin.site.register(Usuario)
admin.site.register(TipoUsuario)