from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=255)
    rut_empresa = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Cliente: {self.usuario.username}"