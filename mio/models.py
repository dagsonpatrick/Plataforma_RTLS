from django.db import models

# Create your models here.
class Mio(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    description= models.CharField(max_length=50, null=False, blank=False)
    ip = models.CharField(max_length=15, null=False, blank=False)
    port = models.IntegerField(null=False, blank=False)
    qtdInputs = models.IntegerField(null=False, blank=False)
    qtdOutputs = models.IntegerField(null=False, blank=False)
    hostListener = models.CharField(max_length=15, null=False, blank=False)
    portListener = models.IntegerField(null=False, blank=False)


