from django.db import models


class Alarme(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=25, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
