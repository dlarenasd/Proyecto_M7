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
    path('inmuebles/crear/', views.InmuebleCreateView.as_view(), name='inmueble_crear'), ###########
    path('inmuebles/editar/<int:id>', views.editar_inmueble, name='inmueble_editar'),
    path('inmuebles/eliminar_inmueble/<int:id>', views.eliminar_inmueble, name='eliminar_inmueble'),
    #path('inmuebles/editar/<int:id>', views.InmuebleUpdateView.as_view(), name='inmueble_editar'),
    #path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
    path('usuario/', views.usuario, name='usuario'),
    path('usuario/actualizar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', views.contacto, name='contacto'),
    #path("select2/", views.select2, name='select2'),
    path('accounts/', include('django.contrib.auth.urls')),
]