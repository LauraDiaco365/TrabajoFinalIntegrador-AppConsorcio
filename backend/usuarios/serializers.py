from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # Exponemos solo los campos seguros y útiles para React
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rol', 'is_active']