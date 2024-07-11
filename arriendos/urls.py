from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from arriendos import views

urlpatterns = [
    path('',views.indexView,name='indice'),
    path('inmuebles',views.InmueblesListView.as_view(),name='inmuebles'),
    path('filtrar-comunas/', views.filtrar_comunas, name='filtrar_comunas'),
    path('buscar_inmuebles/', views.buscar_inmuebles, name='buscar_inmuebles'),
    path('accounts/', include('django.contrib.auth.urls')),
]