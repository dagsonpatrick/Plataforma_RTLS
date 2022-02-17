from django.shortcuts import render
from planos.services import plano_service
from .services import relatorio_service

# Create your views here.


def relatorio_plano(request):
    lista_planos_bd = plano_service.listar_planos()
    return render(request, 'relatorio_plano.html',{'path_foto': request.session['path_foto'],
                                                                    'planos':lista_planos_bd})

def exibir_relatorio_plano(request):

    lista_planos_bd = plano_service.listar_planos()

    if request.method == "POST":
        id_plano = request.POST.get("plano")
        plano_bd =  plano_service.listar_plano_id(id_plano)
        range_data = request.POST.get("range_date")
        relatorio = relatorio_service.construir_relatorio_plano(plano_bd, range_data)


    return render(request,'relatorio/form_exibir_relatorio_plano.html', {'path_foto': request.session['path_foto'],
                                                                          'planos':lista_planos_bd,
                                                                          'dados':relatorio})