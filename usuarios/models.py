from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """Unico modelo de usuario para ambos roles (normalizacion + auth simple)."""
    class Roles(models.TextChoices):
        ADMINISTRADOR = 'administrador', 'Administrador'
        VECINO = 'vecino', 'Vecino'

    rol = models.CharField(max_length=20, choices=Roles.choices)

    def __str__(self):
        return f'{self.username} ({self.rol})'
