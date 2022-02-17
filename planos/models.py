from django.db import models

# Create your models here.

class Plano(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=35, blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    foto = models.FileField(upload_to="planos/")