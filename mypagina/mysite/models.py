from django.db import models

# Create your models here.

class correos_contacto(models.Model):
    nombre = models.TextField()
    correo = models.EmailField()
    telephone = models.IntegerField()
    description = models.TextField()
