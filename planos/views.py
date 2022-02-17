
from django.shortcuts import render,redirect
from .forms import PlanoModelForm
from .models import Plano
from .services import plano_service

# Create your views here.

def cadastrar_plano(request):

    if request.method == "POST":
        form_plano = PlanoModelForm(request.POST, request.FILES)
        if form_plano.is_valid():
            form_plano.save()
            return redirect('listar_planos')
    else:
        form_plano = PlanoModelForm()
    return render(request,'plano/form_cadastrar_plano.html',{"form_plano": form_plano,'path_foto': request.session['path_foto']})

def listar_planos(request):
    planos = plano_service.listar_planos()
    return render(request, 'plano/listar_planos.html',{'planos':planos,'path_foto': request.session['path_foto']})

def remover_plano(request, id):
    plano_bd = plano_service.listar_plano_id(id)
    if request.method == "POST":
        plano_service.remover_plano(plano_bd)
        return redirect('listar_planos')
    return render(request, 'plano/confirma_exclusao.html', {'plano':plano_bd,'path_foto': request.session['path_foto']})

def editar_plano(request, id):
    plano = plano_service.listar_plano_id(id)
    form_plano = PlanoModelForm(request.POST, request.FILES)

    if form_plano.is_valid():
        nome = form_plano.cleaned_data["nome"]
        descricao = form_plano.cleaned_data["descricao"]
        foto = form_plano.cleaned_data["foto"]

        plano_novo = Plano(nome=nome,
                           descricao=descricao,
                           foto=foto)
        plano_service.editar_plano(plano, plano_novo)
        return redirect('listar_planos')
    return render(request, 'plano/form_edit_plano.html', {'plano': plano,'path_foto': request.session['path_foto']})



