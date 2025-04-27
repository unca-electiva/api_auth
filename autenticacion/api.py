from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from autenticacion.models import Anuncio, Usuario
from autenticacion.serializers import AnuncioSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user)
