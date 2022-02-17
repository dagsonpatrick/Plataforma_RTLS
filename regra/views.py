from django.shortcuts import render, redirect
from .forms import RegraForm
from .models import Regra
from .services import regra_service
from planos.services import plano_service
from mio.services import mio_service


# Create your views here.

def cadastrar_regra(request):

    planos_bd = plano_service.listar_planos()

    mios_bd = mio_service.listar_mios()


    if request.method == "POST":
        form_regra = RegraForm(request.POST)
        if form_regra.is_valid():
            name = form_regra.cleaned_data["name"]
            description = form_regra.cleaned_data["description"]
            tempPermanencia = form_regra.cleaned_data["tempPermanencia"]

            plan = form_regra.cleaned_data["plan"]
            mio = form_regra.cleaned_data["mio"]
            event = form_regra.cleaned_data["event"]
            action = form_regra.cleaned_data["action"]
            portout = form_regra.cleaned_data["portout"]
            portin = form_regra.cleaned_data["portin"]
            state = form_regra.cleaned_data["state"]


            regra_nova = Regra(name = name,
                               description=description,
                               tempPermanencia=tempPermanencia,
                               plan = plan,
                               mio = mio,
                               event = event,
                               action = action,
                               portout = portout,
                               portin = portin,
                               state=state)

            regra_service.cadastrar_regra(regra_nova)
            return redirect('home')
    else:
        form_regra = RegraForm()
    return render(request, 'regra/form_cadastrar_regra.html', {'form_regra': form_regra, 'planos': planos_bd, 'mios': mios_bd,  'path_foto': request.session['path_foto']})
