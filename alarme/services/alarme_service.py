from ..models import Alarme


def cadastrar_alarme(ativo):
    Alarme.objects.create(name = ativo.name,
                         description = ativo.description)

def listar_alarmes():
    return Alarme.objects.order_by("id").all()

def listar_alarme_id(id):
    return Alarme.objects.get(id=id)

def remover_alarme(alarme_bd):
    alarme_bd.delete()

def editar_alarme(alarme, alarme_novo):
    alarme.name = alarme_novo.name
    alarme.description = alarme_novo.description
    alarme.save(force_update=True)