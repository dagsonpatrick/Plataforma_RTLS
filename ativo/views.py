from django.shortcuts import render, redirect
from .forms  import AtivoForm
from .models import Ativo
from .services import ativo_service
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def cadastrar_ativo(request):
    if request.method == "POST":
        form_ativo = AtivoForm(request.POST)
        if form_ativo.is_valid():
            name = form_ativo.cleaned_data["name"]
            description = form_ativo.cleaned_data["description"]
            ativo_novo = Ativo(description=description,
                               name=name,
                               statusAssociacao=0)
            ativo_service.cadastrar_ativo(ativo_novo)
            return redirect('listar_ativos')
    else:
        form_ativo = AtivoForm()
    return render(request, 'ativo/form_cadastrar_ativo.html', {'form_ativo': form_ativo,'path_foto': request.session['path_foto']})

def listar_ativos(request):
    ativos = ativo_service.listar_ativos()
    return render(request, 'ativo/form_listar_ativos.html', {'ativos': ativos,'path_foto': request.session['path_foto']})

def remover_ativo(request, id):
    ativo_bd = ativo_service.listar_ativo_id(id)
    if request.method == "POST":
        ativo_service.remover_ativo(ativo_bd)
        return redirect('listar_ativos')
    return render(request, 'ativo/confirma_exclusao.html', {'ativo':ativo_bd,'path_foto': request.session['path_foto']})

def editar_ativo(request, id):
    ativo = ativo_service.listar_ativo_id(id)
    form_ativo = AtivoForm(request.POST)

    if form_ativo.is_valid():
        name = form_ativo.cleaned_data["name"]
        description = form_ativo.cleaned_data["description"]
        ativo_novo = Ativo(name=name,description=description)
        ativo_service.editar_ativo(ativo, ativo_novo)

        return redirect('listar_ativos')
    return render(request, 'ativo/form_editar_ativo.html', {'ativo': ativo,'path_foto': request.session['path_foto']})