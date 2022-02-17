from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar_anchor/', cadastrar_anchor, name='cadastrar_anchor'),
    path('listar_anchors/', listar_anchors, name='listar_anchors'),
    path('editar_anchor/<int:id>', editar_anchor, name='editar_anchor'),
    path('remover_anchor/<int:id>', remover_anchor, name='remover_anchor'),




]