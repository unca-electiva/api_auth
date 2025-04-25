from rest_framework import viewsets

from autenticacion.models import Anuncio, Usuario
from autenticacion.serializers import AnuncioSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user)
