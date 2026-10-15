from rest_framework import serializers
from .models import Gasto, Liquidacion, Pago

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class LiquidacionSerializer(serializers.ModelSerializer):
    monto_total = serializers.ReadOnlyField()

    class Meta:
        model = Liquidacion
        fields = '__all__'