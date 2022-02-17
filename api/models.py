from django.db import models
from anchor.models import Anchor
from tag.models import Tag
from collaborator.models import Collaborator
# Create your models here.

class Evento(models.Model):

    idanchor = models.ForeignKey(Anchor, null=False, on_delete=models.CASCADE)
    idtag = models.ForeignKey(Tag, null=False, on_delete=models.CASCADE)
    idcolaborador = models.ForeignKey(Collaborator, null=True, blank=True, on_delete=models.CASCADE)
    dtInicio = models.DateTimeField(null=False, blank=False)
    dtFim = models.DateTimeField(null=True, blank=True)
    permanencia = models.TimeField(null=True,blank=True)
    status = models.IntegerField(null=False, blank=False)

class Dev(models.Model):

    address= models.CharField(max_length=15, null=False, blank=False)
    place_id = models.IntegerField(null=False, blank=False)
    place_name = models.CharField(max_length=32,null=False, blank=False)
    utcdate = models.DateTimeField()
    connector_utcdate = models.DateTimeField()

class EventoDevAWS(models.Model):

    name = models.CharField(max_length=15, null=False, blank=False)
    place_name = models.CharField(max_length=32, null=False, blank=False)
    distance = models.IntegerField(null=False, blank=False)
    last_seen = models.DateTimeField()
    utcdate = models.DateTimeField()

class InfoEvento(models.Model):

    description_tag = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    permanencia = models.CharField(max_length=15, null=False, blank=False)

class InfoPlanta(models.Model):
    id_plano = models.IntegerField(null=True, blank=True)
    name_plano = models.CharField(max_length=50, null=False, blank=False)
    description_plano = models.CharField(max_length=50, null=False, blank=False)
    foto_plano = models.CharField(max_length=100, null=False, blank=False)
    qtd_colaborador = models.IntegerField(null=False, blank=False)



