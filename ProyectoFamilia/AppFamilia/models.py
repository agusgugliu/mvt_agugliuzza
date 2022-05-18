from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from sqlalchemy import null

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero_documento = models.IntegerField()
    numero_telefono = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)