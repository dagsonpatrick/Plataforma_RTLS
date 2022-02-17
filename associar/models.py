
from django.db import models
# Create your models here.
from collaborator.models import Collaborator
from tag.models import Tag

from planos.models import Plano
from anchor.models import Anchor
from ativo.models import Ativo


class AssociacaoCollaborator(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Tag, null=False,blank=False, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, null=False, on_delete=models.CASCADE)

class AssociacaoAnchor(models.Model):
    id = models.BigAutoField(primary_key=True)
    plano = models.ForeignKey(Plano, null=False, on_delete=models.CASCADE)
    anchor = models.ForeignKey(Anchor, null=False, on_delete=models.CASCADE)

class AssociacaoAtivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Tag, null=False, blank=False, on_delete=models.CASCADE)
    ativo = models.ForeignKey(Ativo, null=False, on_delete=models.CASCADE)