from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Consorcio(models.Model):
    administrador = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        related_name='consorcios_administrados',
    )
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    cuit = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    consorcio = models.ForeignKey(
        Consorcio,
        on_delete=models.CASCADE,
        related_name='unidades',
    )
    propietario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='unidades',
    )
    numero = models.CharField(max_length=10)          # ej: "3B"
    piso = models.CharField(max_length=10, blank=True)
    porcentaje_fiscal = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Porcentaje (0 a 100) que aporta la unidad al prorrateo.',
    )

    class Meta:
        unique_together = ('consorcio', 'numero')
        ordering = ['numero']

    def __str__(self):
        return f'{self.consorcio.nombre} - Unidad {self.numero}'