from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    documento_identidad = models.CharField(max_length=15, verbose_name='Número de documento', unique=True)
    domicilio = models.CharField(max_length=250)


class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    precio_inicial = models.DecimalField(decimal_places=2, max_digits=10)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    publicado_por = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='anuncios_publicados')
