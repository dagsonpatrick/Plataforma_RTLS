from tag.models import Tag
from planos.models import Plano
from anchor.models import Anchor
from ..models import AssociacaoCollaborator
from ..models import AssociacaoAnchor
from ..models import AssociacaoAtivo




def listar_associacoes_ativos():
    return AssociacaoAtivo.objects.all()

def cadastrar_associacao_ativo(associacao):
    AssociacaoAtivo.objects.create(tag=associacao.tag,ativo_id=associacao.ativo.id)
    atualiza_statusAssociacao(associacao.ativo, 1)
    atualiza_statusAssociacao(associacao.tag, 1)

def listar_associacao_ativo_id(id):
    return AssociacaoAtivo.objects.get(id=id)
def remover_associacao_ativo(associacao):
    associacao.delete()
    atualiza_statusAssociacao(associacao.ativo, 0)
    atualiza_statusAssociacao(associacao.tag, 0)


def listar_associacoes_colaboradores():
    return AssociacaoCollaborator.objects.all()
def listar_associacao_colaborador_id(id):
    return AssociacaoCollaborator.objects.get(id=id)
def cadastrar_associacao_colaborador(associacao):
    AssociacaoCollaborator.objects.create(tag=associacao.tag,
                                          collaborator_id=associacao.collaborator.id)
    atualiza_statusAssociacao(associacao.collaborator,1)
    atualiza_statusAssociacao(associacao.tag, 1)

def atualiza_statusAssociacao(colaborador, status):
    colaborador.statusAssociacao = status
    colaborador.save(force_update=True)


def remover_associacao_colaborador(associacao):
    associacao.delete()
    atualiza_statusAssociacao(associacao.collaborator, 0)
    atualiza_statusAssociacao(associacao.tag, 0)

def buscar_colaborador_ass_tag(idtag):
    try:
        return AssociacaoCollaborator.objects.get(tag_id=idtag)
    except AssociacaoCollaborator.DoesNotExist:
        return None

def listar_tags():
    return Tag.objects.all()
def listar_planos():
        return Plano.objects.all()
def listar_anchor():
    return Anchor.objects.all()

def cadastrar_associacao_anchor(anchor):
    AssociacaoAnchor.objects.create(anchor_id=anchor.anchor.id,
                              plano_id=anchor.plano.id)
def listar_associacoes_anchors():
    return AssociacaoAnchor.objects.all()
def listar_associacao_anchor_id(id):
    return AssociacaoAnchor.objects.get(id=id)
def remover_associacao_anchor(associacao_bd):
    associacao_bd.delete()