from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets

from autenticacion.models import Anuncio
from autenticacion.serializers import AnuncioSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    permission_classes = [TokenHasReadWriteScope]

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user)
