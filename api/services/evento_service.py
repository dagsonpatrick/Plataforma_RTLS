from django.http import Http404

from ..models import Evento


def listar_eventos():
    eventos = Evento.objects.all()
    return eventos

def cadastrar_evento(evento):
    return Evento.objects.create(idanchor = evento.idanchor,
                                 idtag = evento.idtag,
                                 idcolaborador = evento.idcolaborador,
                                 dtInicio = evento.dtInicio,
                                 dtFim =  evento.dtFim,
                                 permanencia = evento.permanencia,
                                 status = evento.status)

def listar_evento_id(id):
    try:
        return Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        raise Http404

def editar_evento(evento_antigo, evento_novo):
    evento_antigo.idanchor = evento_novo.idanchor
    evento_antigo.idtag = evento_novo.idtag
    evento_antigo.idcolaborador = evento_novo.idcolaborador
    evento_antigo.dtInicio = evento_novo.dtInicio
    evento_antigo.dtFim = evento_novo.dtFim
    evento_antigo.permanencia = evento_novo.permanencia
    evento_antigo.status = evento_novo.status
    evento_antigo.save(force_update=True)

def remover_evento(evento):
    evento.delete()