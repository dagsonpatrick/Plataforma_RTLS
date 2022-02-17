from django.shortcuts import render
from planos.services import plano_service
from monitor.services import monitor_service

def visualizar_planta(request):
    planos = plano_service.listar_status_planos()
    return render(request, 'visualizar_planta.html', {'planos': planos, 'path_foto': request.session['path_foto']})

def visualizar_plano_planta(request, id):

    planoSelecionado = monitor_service.listar_plano_id(id)
    anchorsPlano = monitor_service.buscar_anchors_plano(planoSelecionado)
    listAnchors = monitor_service.buscar_info_anchors(anchorsPlano)

    eventos_anchors = monitor_service.buscar_evento_anchors(anchorsPlano)
    qtd_tags = len(eventos_anchors)

    return render(request, 'visualizacao/visualizar_plano_planta.html', {'path_foto': request.session['path_foto'],
                                                                     'plano': planoSelecionado,
                                                                     'qtd_tags': qtd_tags,
                                                                     'anchors': listAnchors,
                                                                     'eventos': eventos_anchors})
