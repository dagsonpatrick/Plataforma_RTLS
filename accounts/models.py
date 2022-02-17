from django.db import models
from django.contrib.auth.models import User
import os
import uuid

# Create your models here.

'''class User(models.Model):

    username = models.CharField(max_length=20, null=False,blank=False)
    first_name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    email =  models.EmailField(max_length=70, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
uuid.uuid4()
'''

def get_file_path(instance,filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(),ext)
    return os.path.join("fotoPerfilUsuario/",filename)

class FotoUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    #foto = models.FileField(upload_to="fotoPerfilUsuario/")
    foto = models.FileField(upload_to=get_file_path)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)



