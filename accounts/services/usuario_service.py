from ..models import FotoUser
from django.contrib.auth.models import User


def cadastrar_foto(usuario):
    FotoUser.objects.create(foto=usuario.foto, usuario = usuario.usuario )

def get_usuario_foto(id):
    return FotoUser.objects.get(usuario_id=id)


def editar_foto(foto_bd, foto_nova):
    foto_bd.foto = foto_nova.foto
    foto_bd.save(force_update=True)

def get_usuario_id(id):
    return User.objects.get(id=id)

def remover_usuario(usuario_bd):
    usuario_bd.delete()

def get_path_foto(iduser):
    path = get_usuario_foto(iduser)
    return path.foto