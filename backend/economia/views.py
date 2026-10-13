from rest_framework import viewsets
from .models import Gasto, Liquidacion, Pago
from .serializers import GastoSerializer, LiquidacionSerializer, PagoSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Liquidacion.objects.all()
    serializer_class = LiquidacionSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer