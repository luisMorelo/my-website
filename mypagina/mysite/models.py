from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.TextField()
    correo = models.EmailField()
    telephono = models.IntegerField()
    description = models.TextField()
