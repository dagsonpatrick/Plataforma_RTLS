from api.models import Evento
from collaborator.models import Collaborator
from monitor.services import monitor_service
import json

def construir_relatorio_plano(plano, rangeData):
    jsonData = {'relatorio_plano': []}
    jsonAcesso = {'acessos': []}
    jsonMatriz = []

    dtInicio = rangeData[:10]
    dtFim = rangeData[13:23]

    aI = dtInicio[6:10]
    mI = dtInicio[:2]
    dI = dtInicio[3:5]
    dtInicio = aI+'-'+mI+'-'+dI+"T"+"00:00:00+00:00"

    aF = dtFim[6:10]
    mF = dtFim[:2]
    dF = dtFim[3:5]
    dtFim = aF + '-' + mF + '-' + dF+"T"+"23:59:59+00:00"

    # 2019-10-07T17:49:34+03:00
    #min_date = datetime.strptime(dtInicio, '%Y-%m-%d %H:%M:%S')
    #max_date = datetime.strptime(dtFim, '%Y-%m-%d %H:%M:%S')
    #eventos = Evento.objects.get()
    #lista_colaboradores = Evento.objects.filter()

    anchors_plano = monitor_service.buscar_anchors_plano(plano)
    ids_anchors = []
    for i in anchors_plano:
        ids_anchors.append(i.anchor.id)

    eventos_plano = Evento.objects.filter(idanchor__in=[id for id in ids_anchors], dtInicio__gte=dtInicio, dtFim__lte=dtFim)
    qtd_eventos = len(eventos_plano)

    jsonAcesso['acessos'].append(['Task', str(qtd_eventos)])
    jsonMatriz.append(['Task', str(qtd_eventos)])

    colaboradores = eventos_plano.filter().values('idcolaborador').distinct()
    qtd_colaboradores = len(colaboradores)

    colaboradores_online =  eventos_plano.filter(status=1)
    qtd_online = len(colaboradores_online)

    #colaboradores_offline = eventos_plano.filter(status=0).values('idcolaborador').distinct()
    qtd_offline = 5 - qtd_online

    lista_colaboradores = Collaborator.objects.filter(id__in=[id['idcolaborador'] for id in colaboradores])

    for colaborador in lista_colaboradores:
        qtd = eventos_plano.filter(idcolaborador=colaborador.id).count()
        jsonAcesso['acessos'].append([colaborador.first_name, qtd])
        jsonMatriz.append([colaborador.first_name, qtd])

    acessos=json.dumps(jsonAcesso['acessos'])
    jsonData['relatorio_plano'].append({'eventos_plano': eventos_plano,
                                    'qtd_eventos': qtd_eventos,
                                    'lista_colaboradores': lista_colaboradores,
                                    'qtd_colaboradores': qtd_colaboradores,
                                    'acessos': jsonMatriz,
                                    'colaboradores_online':colaboradores_online,
                                    'qtd_online': qtd_online,
                                    'qtd_offline': qtd_offline,
                                    'plano': plano })

    return jsonData


