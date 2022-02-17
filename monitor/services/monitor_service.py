from planos.models import Plano
from coletor.models import Coletor
from associar.models import AssociacaoAnchor
from anchor.models import Anchor
from api.models import Evento

from api.models import InfoEvento
from api.models import InfoPlanta
from planos.services import plano_service


def listar_planos():
    return Plano.objects.order_by("id").all()

def listar_plano_id(id):
    return Plano.objects.get(id=id)

def listar_planos_selecionados(ids_planos):
    return Plano.objects.filter(id__in=[id for id in ids_planos])

def listar_planos_selecionados_dep(ids_planos_select):
    planos = Plano.objects.filter(id__in=[id for id in ids_planos_select])
    json = {'planos':[]}

    for plano in planos:
        ass_anchors_plano = buscar_anchors_plano(plano)
        list_desc_anchors = buscar_info_anchors(ass_anchors_plano)
        lista_eventos = buscar_evento_anchors(ass_anchors_plano)

        json['planos'].append({'idplano': plano.id,
                               'nome': plano.nome,
                               'descricao': plano.descricao,
                               'foto': plano.foto,
                               'anchors':list_desc_anchors,
                               'eventos':lista_eventos,
                               'qtd_tags':len(lista_eventos)})
    return json

def buscar_evento_anchors(anchorsPlano):
    ids_anchors = []
    for anchor in anchorsPlano:
        ids_anchors.append(anchor.anchor_id)
    return Evento.objects.filter(idanchor_id__in=[id for id in ids_anchors],status=1)

def buscar_info_anchors(anchors):
    ids_anchors = []
    for anchor in anchors:
        ids_anchors.append(anchor.anchor_id)
    return Anchor.objects.filter(id__in=[id for id in ids_anchors])

def buscar_anchors_plano(plano):
    return AssociacaoAnchor.objects.filter(plano_id=plano.id)

def buscar_anchors_planos(planos):
    for p in planos:
        print(p.id)

    #return AssociacaoAnchor.objects.filter(plano_id=planos.id)

def buscar_distict_coletor():
    return Coletor.objects.filter().values('address').distinct()

def listar_planos_selecionados_site(ids_planos_select):
    planos = Plano.objects.filter(id__in=[id for id in ids_planos_select])
    json = {'planos':[]}

    for plano in planos:
        ass_anchors_plano = buscar_anchors_plano(plano)

        lista_eventos = buscar_evento_anchors(ass_anchors_plano)

        json['planos'].append({'idplano': plano.id,
                               'nome': plano.nome,
                               'descricao': plano.descricao,
                               'foto': plano.foto,
                               'eventos':lista_eventos,
                               'qtd_tags':len(lista_eventos)})
    return json

def create_info_evento(eventos):
    list_evento = []
    for evento in eventos:
        info_evento = InfoEvento(description_tag=evento.idtag.description,
                                 first_name=evento.idcolaborador.first_name,
                                 last_name=evento.idcolaborador.last_name,
                                 foto=evento.idcolaborador.foto,
                                 permanencia=evento.permanencia)
        list_evento.append(info_evento)
    return list_evento

def create_info_planta():

    list_plantas = []
    lista_planos = plano_service.listar_status_planos()

    for plano in lista_planos['status_planta']:
        info_planta = InfoPlanta(id_plano = plano['plano'].id,
                                 name_plano=plano['plano'].nome,
                                 description_plano=plano['plano'].descricao,
                                 foto_plano=plano['plano'].foto,
                                 qtd_colaborador=plano['qtd_eventos'])
        list_plantas.append(info_planta)

    return list_plantas
