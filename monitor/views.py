from django.shortcuts import render
from .services import monitor_service
from datetime import datetime
# Create your views here.


def monitorar_plano(request):
    lista_planos_bd = monitor_service.listar_planos()
    return render(request, 'form_monitoramento.html',{'path_foto': request.session['path_foto'],
                                                                    'planos':lista_planos_bd})

def listar_plano_monitoramento(request):

    lista_planos_bd = monitor_service.listar_planos()

    if request.method == "POST":
        id_plano = request.POST.get("plano")
        planoSelecionado =  monitor_service.listar_plano_id(id_plano)
        anchorsPlano = monitor_service.buscar_anchors_plano(planoSelecionado)
        listAnchors = monitor_service.buscar_info_anchors(anchorsPlano)

        eventos_anchors = monitor_service.buscar_evento_anchors(anchorsPlano)
        qtd_tags = len(eventos_anchors)
    return render(request, 'monitoramento/form_listar_planos.html', {'path_foto': request.session['path_foto'],
                                                                     'planos':lista_planos_bd,
                                                                     'plano':planoSelecionado,
                                                                     'qtd_tags':qtd_tags,
                                                                     'anchors': listAnchors,
                                                                     'eventos':eventos_anchors } )


def monitorar_departamento(request):
    lista_planos_bd = monitor_service.listar_planos()
    return render(request, 'form_monitoramento_dep.html', {'path_foto': request.session['path_foto'],
                                                       'planos': lista_planos_bd})

def listar_planos_departamento(request):

    lista_planos_bd = monitor_service.listar_planos()

    if request.method == "POST":
        id_planos_select = request.POST.getlist("plano")
        lista_planos_select = monitor_service.listar_planos_selecionados_dep(id_planos_select)

        '''for i in x.planos[0].anchors:
            print(i.description)
        for i in x.planos[0].eventos:
            print(i.idtag.description)
            print(i.permanencia)'''

    return render(request, 'monitoramento/form_listar_planos_dep.html', {'path_foto': request.session['path_foto'],
                                                                         'planos':lista_planos_bd,
                                                                         'lista_planos_select':lista_planos_select} )

def monitorar_site(request):
    lista_planos_bd = monitor_service.listar_planos()
    return render(request, 'form_monitoramento_site.html', {'path_foto': request.session['path_foto'],
                                                           'planos': lista_planos_bd})

def listar_planos_site(request):

    lista_planos_bd = monitor_service.listar_planos()

    if request.method == "POST":
        id_planos_select = request.POST.getlist("plano")
        lista_planos_select = monitor_service.listar_planos_selecionados_site(id_planos_select)


    return render(request, 'monitoramento/form_listar_planos_site.html', {'path_foto': request.session['path_foto'],
                                                                          'planos':lista_planos_bd,
                                                                          'lista_planos_select': lista_planos_select})