from django.db import models
from planos.models import Plano
from mio.models import Mio

class Regra(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
    tempPermanencia = models.TimeField(null=True, blank=True)

    plan = models.ForeignKey(Plano, null=False, on_delete=models.CASCADE)
    mio = models.ForeignKey(Mio, null=False, on_delete=models.CASCADE)

    event = models.CharField(max_length=15, null=False, blank=False)
    action = models.CharField(max_length=15, null=False, blank=False)
    portout = models.IntegerField(null=False, blank=False)
    portin = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)




