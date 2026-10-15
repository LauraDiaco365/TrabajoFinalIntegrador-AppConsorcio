from rest_framework import viewsets
from .models import Consorcio, Unidad
from .serializers import ConsorcioSerializer, UnidadSerializer

class ConsorcioViewSet(viewsets.ModelViewSet):
    queryset = Consorcio.objects.all()
    serializer_class = ConsorcioSerializer

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer