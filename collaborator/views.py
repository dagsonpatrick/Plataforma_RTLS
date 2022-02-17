from django.shortcuts import render, redirect
from .forms import CollaboratorForm
from .models import Collaborator
from .services import collaborator_service

# Create your views here.

def cadastrar_collaborator(request):
    if request.method == "POST":
        form_collaborator = CollaboratorForm(request.POST, request.FILES)
        if form_collaborator.is_valid():
            first_name = form_collaborator.cleaned_data["first_name"]
            last_name = form_collaborator.cleaned_data["last_name"]
            email = form_collaborator.cleaned_data["email"]
            foto = form_collaborator.cleaned_data["foto"]
            collaborator_nova = Collaborator(first_name=first_name,
                                             last_name=last_name,
                                             email=email,
                                             foto=foto,
                                             statusAssociacao=0)

            collaborator_service.cadastrar_collaborator(collaborator_nova)
            return redirect('listar_collaborators')
    else:
        form_collaborator = CollaboratorForm()
    return render(request, 'collaborator/form_cadastrar_collaborator.html', {'form_collaborator': form_collaborator,'path_foto': request.session['path_foto']})

def listar_collaborators(request):
    collaborators = collaborator_service.listar_collaborators()
    return render(request, 'collaborator/form_listar_collaborators.html', {'collaborators': collaborators,'path_foto': request.session['path_foto']})

def editar_collaborator(request, id):
    collaborator = collaborator_service.listar_collaborator_id(id)
    form_collaborator = CollaboratorForm(request.POST, request.FILES)

    if form_collaborator.is_valid():
        first_name = form_collaborator.cleaned_data["first_name"]
        last_name = form_collaborator.cleaned_data["last_name"]
        email = form_collaborator.cleaned_data["email"]
        foto = form_collaborator.cleaned_data["foto"]
        collaborator_nova = Collaborator(first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         foto=foto)

        collaborator_service.editar_collaborator(collaborator, collaborator_nova)
        return redirect('listar_collaborators')
    return render(request, 'collaborator/form_editar_collaborator.html', {'collaborator': collaborator,'path_foto': request.session['path_foto']})

def remover_collaborator(request, id):
    collaborator_bd = collaborator_service.listar_collaborator_id(id)
    if request.method == "POST":
        collaborator_service.remover_collaborator(collaborator_bd)
        return redirect('listar_collaborators')
    return render(request, 'collaborator/confirma_exclusao.html', {'collaborator':collaborator_bd,'path_foto': request.session['path_foto']})