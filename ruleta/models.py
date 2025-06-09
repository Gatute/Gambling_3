from django.db import models
from users.models import PerfilUsuario


class Apuesta(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    resultado = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
