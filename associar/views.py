from django.shortcuts import render, redirect
from .forms import ColaboradorForm, AnchorForm, AtivoForm
from .entidades.associarCollaborator import AssociarCollaborator
from .entidades.associarAnchor import AssociarAnchor
from .entidades.associarAtivo import AssociarAtivo
from .services import associar_service
from collaborator.services import collaborator_service
from tag.services import tag_service
from ativo.services import ativo_service
from tag.services import tag_service


def associar_colaborador(request):
    lista_colaboradores = collaborator_service.listar_colaboradores_nao_associados()
    lista_tag = tag_service.listar_tags_nao_associadas()
    associacoes = associar_service.listar_associacoes_colaboradores()

    if request.method == "POST":
        form_associacao = ColaboradorForm(request.POST)
        if form_associacao.is_valid():
            tag = form_associacao.cleaned_data["tag"]
            collaborator = form_associacao.cleaned_data["collaborator"]
            associacao_nova = AssociarCollaborator(tag=tag,
                                 collaborator=collaborator)
            associar_service.cadastrar_associacao_colaborador(associacao_nova)
            return render(request, 'associacao/form_cadastrar_associacao_colaborador.html', { 'associacoes': associacoes, 'lista_tag':lista_tag, 'lista_colaboradores':lista_colaboradores, 'form_associacao': form_associacao, 'path_foto': request.session['path_foto']})
    else:
        form_associacao = ColaboradorForm()
    return render(request, 'associacao/form_cadastrar_associacao_colaborador.html', { 'associacoes': associacoes, 'lista_tag':lista_tag, 'lista_colaboradores':lista_colaboradores, 'form_associacao': form_associacao, 'path_foto': request.session['path_foto']})
def listar_associacoes_colaboradores(request):
    associacoes = associar_service.listar_associacoes_colaboradores()
    return render(request, 'associacao/form_listar_associacoes_colaboradores.html', {'associacoes': associacoes, 'path_foto': request.session['path_foto']})
def remover_associacao_colaborador(request, id):
    associacao_bd = associar_service.listar_associacao_colaborador_id(id)
    if request.method == "POST":
        associar_service.remover_associacao_colaborador(associacao_bd)
        return redirect('associar_colaborador')
    return render(request, 'associacao/confirma_exclusao_ass_colaborador.html', {'associacao':associacao_bd,'path_foto': request.session['path_foto']})


def associar_anchor(request):
    lista_planos = associar_service.listar_planos()
    lista_anchor = associar_service.listar_anchor()
    associacoes = associar_service.listar_associacoes_anchors()

    if request.method == "POST":
        form_associacao = AnchorForm(request.POST)

        if form_associacao.is_valid():
            anchor = form_associacao.cleaned_data["anchor"]
            plano = form_associacao.cleaned_data["plano"]
            associacao_nova = AssociarAnchor(anchor=anchor, plano=plano )
            associar_service.cadastrar_associacao_anchor(associacao_nova)
            return render(request, 'associacao/form_cadastrar_associacao_anchor.html', {'associacoes': associacoes, 'lista_anchor':lista_anchor, 'lista_planos':lista_planos, 'form_associacao': form_associacao, 'path_foto': request.session['path_foto']})
    else:
        form_associacao = AnchorForm()

    return render(request, 'associacao/form_cadastrar_associacao_anchor.html', {'associacoes': associacoes, 'lista_anchor':lista_anchor, 'lista_planos':lista_planos, 'form_associacao': form_associacao, 'path_foto': request.session['path_foto']})

def listar_associacoes_anchors(request):
    associacoes = associar_service.listar_associacoes_anchors()
    return render(request, 'associacao/form_listar_associacoes_anchor.html', {'associacoes': associacoes, 'path_foto': request.session['path_foto']})

def remover_associacao_anchor(request, id):
    associacao_bd = associar_service.listar_associacao_anchor_id(id)
    if request.method == "POST":
        associar_service.remover_associacao_anchor(associacao_bd)
        return redirect('associar_anchor')
    return render(request, 'associacao/confirma_exclusao_ass_anchor.html', {'associacao':associacao_bd,'path_foto': request.session['path_foto']})


def associar_ativo(request):
    lista_ativos = ativo_service.listar_ativos_nao_associados()
    lista_tag = tag_service.listar_tags_nao_associadas()
    associacoes = associar_service.listar_associacoes_ativos()

    if request.method == "POST":
        form_associacao = AtivoForm(request.POST)
        if form_associacao.is_valid():
            tag = form_associacao.cleaned_data["tag"]
            ativo = form_associacao.cleaned_data["ativo"]
            associacao_nova = AssociarAtivo(tag=tag, ativo=ativo)
            associar_service.cadastrar_associacao_ativo(associacao_nova)

            return render(request, 'associacao/form_cadastrar_associacao_ativo.html', { 'associacoes': associacoes, 'lista_tag':lista_tag, 'lista_ativos':lista_ativos, 'form_associacao': form_associacao, 'path_foto': request.session['path_foto']})
    else:
        form_associacao = AtivoForm()
    return render(request, 'associacao/form_cadastrar_associacao_ativo.html', { 'associacoes': associacoes, 'lista_tag':lista_tag, 'lista_ativos':lista_ativos, 'form_associacao': form_associacao, 'path_foto': request.session['path_foto']})

def listar_associacoes_ativos(request):
    associacoes = associar_service.listar_associacoes_ativos()
    return render(request, 'associacao/form_listar_associacoes_ativos.html', {'associacoes': associacoes, 'path_foto': request.session['path_foto']})

def remover_associacao_ativo(request, id):
    associacao_bd = associar_service.listar_associacao_ativo_id(id)
    if request.method == "POST":
        associar_service.remover_associacao_ativo(associacao_bd)
        return redirect('associar_ativo')
    return render(request, 'associacao/confirma_exclusao_ass_ativo.html', {'associacao':associacao_bd,'path_foto': request.session['path_foto']})


def exibir_associacoes(request):
    return render(request, 'associacao/form_exibir_associacao.html',{'path_foto': request.session['path_foto']})
def listar_associacoes(request):

    if request.method == "POST":
        associacao = request.POST.get("associacao")
        if associacao == "Ancoras":
           return  redirect(listar_associacoes_anchors)
        if associacao == "Colaboradores":
            return redirect(listar_associacoes_colaboradores)
        if associacao == "Ativos":
            return redirect(listar_associacoes_ativos)

