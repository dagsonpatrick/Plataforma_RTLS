from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar_alarme/', cadastrar_alarme, name='cadastrar_alarme'),
    path('listar_alarmes/', listar_alarmes, name='listar_alarmes'),
    path('editar_alarme/<int:id>', editar_alarme, name='editar_alarme'),
    path('remover_alarme/<int:id>', remover_alarme, name='remover_alarme'),


]