from ..models import Anchor

def cadastrar_anchor(tag):
    Anchor.objects.create(description = tag.description,
                                 address = tag.address)

def listar_anchors():
    return Anchor.objects.all()

def listar_anchor_id(id):
    return Anchor.objects.get(id=id)

def listar_anchor_description(description):
    return Anchor.objects.get(description=description)

def editar_anchor(anchor, anchor_nova):
    anchor.description = anchor_nova.description
    anchor.address = anchor_nova.address
    anchor.save(force_update=True)

def remover_anchor(anchor_bd):
    anchor_bd.delete()