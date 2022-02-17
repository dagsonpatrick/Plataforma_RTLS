
from accounts.models import FotoUser

def get_usuario_foto(id):
    return FotoUser.objects.get(usuario_id=id)

