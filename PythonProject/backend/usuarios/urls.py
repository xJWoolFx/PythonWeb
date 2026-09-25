from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from usuarios.views import listar_usuarios

urlpatterns = [
    path('api/usuarios/', listar_usuarios, name='listar-usuarios'),
]
