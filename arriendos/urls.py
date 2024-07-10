from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from arriendos import views

urlpatterns = [
    path('',views.indexView,name='home'),
]