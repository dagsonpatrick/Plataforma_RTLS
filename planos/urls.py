from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_plano/', cadastrar_plano, name='cadastrar_plano'),
    path('listar_planos/', listar_planos, name='listar_planos'),
    path('remover_plano/<int:id>', remover_plano, name='remover_plano'),
    path('editar_plano/<int:id>', editar_plano, name='editar_plano'),


]