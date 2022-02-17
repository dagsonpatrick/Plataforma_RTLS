from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar_ativo/', cadastrar_ativo, name='cadastrar_ativo'),
    path('listar_ativos/', listar_ativos, name='listar_ativos'),
    path('editar_ativo/<int:id>', editar_ativo, name='editar_ativo'),
    path('remover_ativo/<int:id>', remover_ativo, name='remover_ativo'),


]