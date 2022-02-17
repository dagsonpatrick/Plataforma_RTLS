from django.shortcuts import render, redirect
from .forms import AnchorForm
from .models import Anchor
from .services import anchor_service
# Create your views here.

def cadastrar_anchor(request):
    if request.method == "POST":
        form_anchor = AnchorForm(request.POST)
        if form_anchor.is_valid():
            description = form_anchor.cleaned_data["description"]
            address = form_anchor.cleaned_data["address"]
            anchor_nova = Anchor(description=description,
                           address=address)

            anchor_service.cadastrar_anchor(anchor_nova)
            return redirect('listar_anchors')
    else:
        form_anchor= AnchorForm()
    return render(request, 'anchor/form_cadastrar_anchor.html',{'form_anchor': form_anchor, 'path_foto': request.session['path_foto']})

def listar_anchors(request):
    anchors = anchor_service.listar_anchors()
    return render(request, 'anchor/form_listar_anchors.html', {'anchors': anchors, 'path_foto': request.session['path_foto']})

def editar_anchor(request, id):
    anchor = anchor_service.listar_anchor_id(id)
    form_anchor = AnchorForm(request.POST)

    if form_anchor.is_valid():
        description = form_anchor.cleaned_data["description"]
        address = form_anchor.cleaned_data["address"]

        anchor_nova = Anchor(description=description,
                       address=address)

        anchor_service.editar_anchor(anchor, anchor_nova)
        return redirect('listar_anchors')
    return render(request, 'anchor/form_editar_anchor.html', {'anchor': anchor, 'path_foto': request.session['path_foto']})

def remover_anchor(request, id):
    anchor_bd = anchor_service.listar_anchor_id(id)
    if request.method == "POST":
        anchor_service.remover_anchor(anchor_bd)
        return redirect('listar_anchors')
    return render(request, 'anchor/confirma_exclusao.html', {'anchor': anchor_bd, 'path_foto': request.session['path_foto']})
