from django.urls import path
from .views import *

urlpatterns = [


    path('associar_colaborador/', associar_colaborador, name='associar_colaborador'),
    path('listar_associacoes_colaboradores/', listar_associacoes_colaboradores, name='listar_associacoes_colaboradores'),
    path('remover_associacao_colaborador/<int:id>', remover_associacao_colaborador, name='remover_associacao_colaborador'),

    path('associar_anchor/', associar_anchor, name='associar_anchor'),
    path('listar_associacoes_anchors/', listar_associacoes_anchors, name='listar_associacoes_anchors'),
    path('remover_associacao_anchor/<int:id>', remover_associacao_anchor, name='remover_associacao_anchor'),


    path('associar_ativo/', associar_ativo, name='associar_ativo'),
    path('listar_associacoes_ativos/', listar_associacoes_ativos, name='listar_associacoes_ativos'),
    path('remover_associacao_ativo/<int:id>', remover_associacao_ativo, name='remover_associacao_ativo'),


    path('exibir_associacoes/', exibir_associacoes, name='exibir_associacoes'),
    path('listar_associacoes/', listar_associacoes, name='listar_associacoes'),


]