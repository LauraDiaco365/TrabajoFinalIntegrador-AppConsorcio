from rest_framework import viewsets
from .models import Mantenimiento
from .serializers import MantenimientoSerializer

class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer