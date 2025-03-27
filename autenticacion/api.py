from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from autenticacion.models import Anuncio, Usuario
from autenticacion.serializers import AnuncioSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(id=1)
        serializer.save(publicado_por=usuario)
