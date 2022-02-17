
from django.db import models

# Create your models here.
class Anchor(models.Model):
    id = models.BigAutoField(primary_key=True)
    description= models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=15, null=False, blank=False)
