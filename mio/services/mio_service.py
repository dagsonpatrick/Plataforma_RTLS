from ..models import Mio
import os

def cadastrar_mio(mio):
    Mio.objects.create(name = mio.name,
                       description = mio.description,
                       ip = mio.ip,
                       port = mio.port,
                       qtdInputs = mio.qtdInputs,
                       qtdOutputs = mio.qtdOutputs,
                       hostListener = mio.hostListener,
                       portListener = mio.portListener)

def listar_mios():
    return Mio.objects.order_by("id").all()

def listar_mio_id(id):
    return Mio.objects.get(id=id)

def remover_mio(mio_bd):
    mio_bd.delete()

def editar_mio(mio, mio_nova):
    mio.name = mio_nova.name
    mio.description = mio_nova.description
    mio.ip = mio_nova.ip
    mio.port = mio_nova.port
    mio.qtdInputs = mio_nova.qtdInputs
    mio.qtdOutputs = mio_nova.qtdOutputs
    mio.hostListener = mio_nova.hostListener
    mio.portListener = mio_nova.portListener
    mio.save(force_update=True)

def check_status_mios():
    lista_mios = listar_mios()
    mios =  []
    for mio in lista_mios:
        status = os.system('ping -n 1 {}'.format(mio.ip))
        if status == 0:
            status_io = 'Em funcionamento'
        else:
            status_io = 'Fora de funcionamento'
        status = os.system('ping -n 1 {}'.format(mio.hostListener))
        if status == 0:
            status_service = 'Em funcionamento'
        else:
            status_service = 'Fora de funcionamento'

        mios.append({'name': mio.name,
                     'description': mio.description,
                     'ip': mio.ip,
                     'port': mio.port,
                     'status': status_io,
                     'hostListener': mio.hostListener,
                     'portListener': mio.portListener,
                     'status_service': status_service})
    return mios
