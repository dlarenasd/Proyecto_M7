from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from arriendos import views

urlpatterns = [
    path('',views.indexView,name='indice'),
    path('inmuebles/',views.InmueblesListView.as_view(),name='inmuebles'),
    path('filtrar-comunas/', views.filtrar_comunas, name='filtrar_comunas'),
    path('buscar_inmuebles/', views.buscar_inmuebles, name='buscar_inmuebles'),
    path('inmuebles/ver_inmueble/<int:id>', views.ver_inmueble, name='ver_inmueble'),
    path('inmuebles/editar_inmueble/<int:id>', views.editar_inmueble, name='editar_inmueble'),
    path('inmuebles/eliminar_inmueble/<int:id>', views.eliminar_inmueble, name='eliminar_inmueble'),
    path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', views.contacto, name='contacto'),
    path('accounts/', include('django.contrib.auth.urls')),
]