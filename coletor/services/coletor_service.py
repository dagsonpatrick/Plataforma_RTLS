from ..models import Coletor

def listar_coletor():
    return Coletor.objects.order_by("id").all()