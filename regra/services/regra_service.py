from ..models import Regra

def cadastrar_regra(regra):
    Regra.objects.create(name = regra.name,
                        description = regra.description,
                        tempPermanencia = regra.tempPermanencia,
                        plan = regra.plan,
                        mio = regra.mio,
                        event = regra.event,
                        action = regra.action,
                        portout = regra.portout,
                        portin = regra.portin,
                        state = regra.state)

