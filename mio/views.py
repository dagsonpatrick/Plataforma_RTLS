from django.shortcuts import render, redirect
from .forms import MioForm
from .models import Mio
from .services import mio_service


# Create your views here.

def cadastrar_mio(request):
    if request.method == "POST":
        form_mio = MioForm(request.POST)
        if form_mio.is_valid():
            name = form_mio.cleaned_data["name"]
            description = form_mio.cleaned_data["description"]
            ip = form_mio.cleaned_data["ip"]
            port = form_mio.cleaned_data["port"]
            qtdInputs = form_mio.cleaned_data["qtdInputs"]
            qtdOutputs = form_mio.cleaned_data["qtdOutputs"]
            hostListener = form_mio.cleaned_data["hostListener"]
            portListener = form_mio.cleaned_data["portListener"]


            mio_nova = Mio(name = name,
                           description=description,
                           ip = ip,
                           port = port,
                           qtdInputs = qtdInputs,
                           qtdOutputs = qtdOutputs,
                           hostListener = hostListener,
                           portListener = portListener
                           )

            mio_service.cadastrar_mio(mio_nova)
            return redirect('listar_mios')
    else:
        form_mio = MioForm()
    return render(request, 'mio/form_cadastrar_mio.html', {'form_mio': form_mio,'path_foto': request.session['path_foto']})

def listar_mios(request):
    mios = mio_service.listar_mios()
    return render(request, 'mio/form_listar_mios.html', {'mios': mios,'path_foto': request.session['path_foto']})

def remover_mio(request, id):
    mio_bd = mio_service.listar_mio_id(id)
    if request.method == "POST":
        mio_service.remover_mio(mio_bd)
        return redirect('listar_mios')
    return render(request, 'mio/confirma_exclusao.html', {'mio':mio_bd,'path_foto': request.session['path_foto']})

def editar_mio(request, id):
    mio_bd = mio_service.listar_mio_id(id)

    if request.method == "POST":
        form_mio = MioForm(request.POST)

        if form_mio.is_valid():
            name = form_mio.cleaned_data["name"]
            description = form_mio.cleaned_data["description"]
            ip = form_mio.cleaned_data["ip"]
            port = form_mio.cleaned_data["port"]
            qtdInputs = form_mio.cleaned_data["qtdInputs"]
            qtdOutputs = form_mio.cleaned_data["qtdOutputs"]
            hostListener = form_mio.cleaned_data["hostListener"]
            portListener = form_mio.cleaned_data["portListener"]

            mio_nova = Mio(name=name,
                           description=description,
                           ip=ip,
                           port=port,
                           qtdInputs=qtdInputs,
                           qtdOutputs=qtdOutputs,
                           hostListener=hostListener,
                           portListener=portListener
                           )

            mio_service.editar_mio(mio_bd, mio_nova)
            return redirect('listar_mios')
    else:
        form_mio = MioForm()

    return render(request, 'mio/form_editar_mio.html', {'form_mio':form_mio, 'mio': mio_bd,'path_foto': request.session['path_foto']})

def status_mios(request):
    mios = mio_service.check_status_mios()
    return render(request, 'mio/form_status_mios.html', {'mios': mios, 'path_foto': request.session['path_foto']})