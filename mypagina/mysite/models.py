from django.db import models

# Create your models here.

class contacto(models.Model):
    nombre = models.TextField()
    correo = models.EmailField()
    telephono = models.IntegerField()
    description = models.TextField()
