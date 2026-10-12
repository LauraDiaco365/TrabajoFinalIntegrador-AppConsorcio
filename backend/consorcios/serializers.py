from rest_framework import serializers
from .models import Consorcio, Unidad


class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = "__all__"


class ConsorcioSerializer(serializers.ModelSerializer):
    unidades = UnidadSerializer(many=True, read_only=True)

    class Meta:
        model = Consorcio
        fields = "__all__"
