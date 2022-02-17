from ..models import Plano
from monitor.services import monitor_service
from api.models import Evento
def listar_planos():
    return Plano.objects.order_by("id").all()

def listar_plano_id(id):
    return Plano.objects.get(id=id)

def listar_plano_id(id):
    return Plano.objects.get(id=id)

def remover_plano(plano_bd):
    plano_bd.delete()

def editar_plano(plano_bd, plano_novo):
    plano_bd.nome = plano_novo.nome
    plano_bd.descricao = plano_novo.descricao
    plano_bd.foto = plano_novo.foto
    plano_bd.save(force_update=True)


def listar_status_planos():
    jsonData = {'status_planta': []}
    listPlanos = listar_planos()

    for plano in listPlanos:
        anchors_plano = monitor_service.buscar_anchors_plano(plano)
        ids_anchors = []
        for i in anchors_plano:
            ids_anchors.append(i.anchor.id)

        eventos_plano = Evento.objects.filter(idanchor__in=[id for id in ids_anchors],status=1)
        qtd_eventos = len(eventos_plano)

        jsonData['status_planta'].append({'plano': plano,
                                        'qtd_eventos': qtd_eventos})

    return jsonData