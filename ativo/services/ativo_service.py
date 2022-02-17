from ..models import Ativo


def cadastrar_ativo(ativo):
    Ativo.objects.create(name = ativo.name,
                         description = ativo.description,
                         statusAssociacao = ativo.statusAssociacao)

def listar_ativos():
    return Ativo.objects.order_by("id").all()

def listar_ativos_nao_associados():
    return Ativo.objects.filter(statusAssociacao = 0).order_by("id").all()

def listar_ativo_id(id):
    return Ativo.objects.get(id=id)

def remover_ativo(ativo_bd):
    ativo_bd.delete()

def editar_ativo(ativo, ativo_novo):
    ativo.name = ativo_novo.name
    ativo.description = ativo_novo.description
    ativo.save(force_update=True)