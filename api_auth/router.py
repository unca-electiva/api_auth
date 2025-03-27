from rest_framework import routers

from autenticacion.api import AnuncioViewSet

# Initializar el router de DRF solo una vez
router = routers.DefaultRouter()

# Registrar un ViewSet
router.register(prefix='anuncio', viewset=AnuncioViewSet)

urlpatterns = [
]

urlpatterns += router.urls
