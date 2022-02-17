from django.db import models

# Create your models here.
class Coletor(models.Model):

    id = models.BigAutoField(primary_key=True)

    address= models.CharField(max_length=15, null=False, blank=False)
    place_id = models.IntegerField(null=False, blank=False)
    place_name = models.CharField(max_length=32,null=False, blank=False)
    battery = models.IntegerField(null=False, blank=False)
    temperature = models.IntegerField(null=False, blank=False)
    utcdate = models.DateTimeField()
    connector_utcdate = models.DateTimeField()


