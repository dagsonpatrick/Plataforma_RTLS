from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar_mio/', cadastrar_mio, name='cadastrar_mio'),
    path('listar_mios/', listar_mios, name='listar_mios'),
    path('editar_mio/<int:id>', editar_mio, name='editar_mio'),
    path('remover_mio/<int:id>', remover_mio, name='remover_mio'),

    path('status_mios/', status_mios, name='status_mios'),

]