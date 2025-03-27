from rest_framework import serializers

from autenticacion.models import Anuncio


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            'id',
            'titulo',
            'precio_inicial',
            'activo',
            'publicado_por',
        ]
        read_only_fields = ['publicado_por']
