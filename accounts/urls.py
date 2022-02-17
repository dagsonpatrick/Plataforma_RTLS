from django.urls import path
from .views import *

#app_name = 'accounts'

urlpatterns = [

    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),

    path('perfil_usuario/', perfil_usuario, name='perfil_usuario'),
    path('editar_senha_usuario/', editar_senha_usuario, name='editar_senha_usuario'),
    path('editar_profile_usuario/', editar_profile_usuario, name='editar_profile_usuario'),
    path('editar_foto_usuario/<int:id>', editar_foto_usuario, name='editar_foto_usuario'),

    path('deletar_usuario/<int:id>', deletar_usuario, name='deletar_usuario'),

]
#path('get_foto_path/', get_foto_path, name='get_foto_path'),