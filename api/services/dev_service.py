from django.http import Http404
from ..models import Dev, Evento
from .evento_service import editar_evento
from anchor.services import anchor_service
from tag.services import tag_service
from associar.services import associar_service

def listar_devs():
    devs = Dev.objects.all()
    return devs

def cadastrar_dev(dev):
    return Dev.objects.create(address = dev.address,
                              place_id = dev.place_id,
                              place_name= dev.place_name,
                              utcdate =  dev.utcdate,
                              connector_utcdate = dev.connector_utcdate)

def listar_dev_id(id):
    try:
        return Dev.objects.get(id=id)
    except Dev.DoesNotExist:
        raise Http404

def verifique_dev_exist_id(id):
    try:
        return Dev.objects.get(id=id)
    except Dev.DoesNotExist:
        raise Http404

def verificar_tag_existe(tag, anchor):
    try:
        Evento.objects.get(idtag=tag, idanchor=anchor, status=1)
        status = True
        return status
    except Evento.DoesNotExist:
        status = False
        return status

def verificar_status_tag_anchor(tag, anchor):
    evento_bd = Evento.objects.filter(idtag=tag,idanchor=anchor)
    status=0
    for i in evento_bd:
        status = i.status
    return status

def atualizar_status_tag_anchor(tag, anchor, status):
    evento_antigo = Evento.objects.get(idtag=tag, idanchor=anchor)
    evento_novo = Evento(idanchor=evento_antigo.idanchor,
                         idtag = evento_antigo.idtag,
                         idcolaborador = evento_antigo.idcolaborador,
                         dtInicio = evento_antigo.dtInicio,
                         dtFim = evento_antigo.dtFim,
                         permanencia = evento_antigo.permanencia,
                         status = status)
    editar_evento(evento_antigo,evento_novo)

def verificar_status_tag_ancoras(tag, anchor):
    # SELECT * FROM `api_evento` WHERE idanchor_id != 4 and status=1
    # Evento.objects.filter(idtag=tag, idanchor ! anchor, status=1)
    # Evento.objects.exclude(idanchor__gte=anchor)
    aux = Evento.objects.exclude(idanchor=anchor).filter(idtag=tag, status=1)
    tam = len(aux)
    if tam > 0:
        for i in aux:
            idreg = i.id
            evento_antigo = Evento.objects.get(id=idreg)
            evento_novo = Evento(idanchor=evento_antigo.idanchor,
                                 idtag=evento_antigo.idtag,
                                 idcolaborador=evento_antigo.idcolaborador,
                                 dtInicio=evento_antigo.dtInicio,
                                 dtFim=evento_antigo.dtFim,
                                 permanencia=evento_antigo.permanencia,
                                 status=0)
        editar_evento(evento_antigo, evento_novo)



def verifique_dado(dev):

    anchor = anchor_service.listar_anchor_description(dev.place_name)

    tag = tag_service.listar_tag_address(dev.name)

    #verificar e atualizar o status da tag com outras ancoras
    verificar_status_tag_ancoras(tag, anchor)

    #vericando se a tag existe na tabela api_evento do banco de dados
    status = verificar_tag_existe(tag, anchor)

    colaborador_tag = associar_service.buscar_colaborador_ass_tag(tag.id)



    if status == True:
        #atualiza o registro
        evento_antigo = Evento.objects.get(idtag=tag, idanchor=anchor, status=1)
        permanencia = str( dev.utcdate - evento_antigo.dtInicio)
        evento_antigo.permanencia = permanencia
        evento_antigo.dtFim = dev.utcdate
        editar_evento(evento_antigo,evento_antigo)

    else:
        #Cria um registro novo
        if colaborador_tag == None:
            return Evento.objects.create(idanchor=anchor,
                                         idtag=tag,
                                         dtInicio=dev.utcdate,
                                         dtFim=dev.utcdate,
                                         permanencia="00:00:00",
                                         status=1)
        else:
            return Evento.objects.create(idanchor = anchor,
                                     idtag = tag,
                                     idcolaborador=colaborador_tag.collaborator,
                                     dtInicio =  dev.utcdate,
                                     dtFim =  dev.utcdate,
                                     permanencia =  "00:00:00",
                                     status= 1)


def editar_dev(dev_antigo, dev_novo):
    dev_antigo.address  = dev_novo.address
    dev_antigo.place_id = dev_novo.place_id
    dev_antigo.place_name  = dev_novo.place_name
    dev_antigo.utcdate = dev_novo.utcdate
    dev_antigo.connector_utcdate = dev_novo.connector_utcdate
    dev_antigo.save(force_update=True)

def remover_dev(dev):
    dev.delete()

def remover_dev(dev):
    dev.delete()