
from django.shortcuts import render, redirect
from .forms  import AlarmeForm
from .models import Alarme
from .services import alarme_service

# Create your views here.

def cadastrar_alarme(request):
    if request.method == "POST":
        form_alarme = AlarmeForm(request.POST)
        if form_alarme.is_valid():
            name = form_alarme.cleaned_data["name"]
            description = form_alarme.cleaned_data["description"]

            alarme_novo = Alarme(description=description,
                                 name=name)
            alarme_service.cadastrar_alarme(alarme_novo)
            return redirect('listar_alarmes')
    else:
        form_alarme = AlarmeForm()
    return render(request, 'alarme/form_cadastrar_alarme.html', {'form_alarme': form_alarme,'path_foto': request.session['path_foto']})

def listar_alarmes(request):
    alarmes = alarme_service.listar_alarmes()
    return render(request, 'alarme/form_listar_alarmes.html', {'alarmes': alarmes,'path_foto': request.session['path_foto']})

def remover_alarme(request, id):
    alarme_bd = alarme_service.listar_alarme_id(id)
    if request.method == "POST":
        alarme_service.remover_alarme(alarme_bd)
        return redirect('listar_alarmes')
    return render(request, 'alarme/confirma_exclusao.html', {'alarme':alarme_bd,'path_foto': request.session['path_foto']})

def editar_alarme(request, id):
    alarme = alarme_service.listar_alarme_id(id)
    form_alarme = AlarmeForm(request.POST)

    if form_alarme.is_valid():
        name = form_alarme.cleaned_data["name"]
        description = form_alarme.cleaned_data["description"]
        alarme_novo = Alarme(name=name,description=description)
        alarme_service.editar_alarme(alarme, alarme_novo)

        return redirect('listar_alarmes')
    return render(request, 'alarme/form_editar_alarme.html', {'alarme': alarme,'path_foto': request.session['path_foto']})