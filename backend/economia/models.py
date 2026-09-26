from decimal import Decimal
from django.db import models


class Gasto(models.Model):
    class Tipos(models.TextChoices):
        ORDINARIO = 'ordinario', 'Ordinario'
        EXTRAORDINARIO = 'extraordinario', 'Extraordinario'

    consorcio = models.ForeignKey(
        'consorcios.Consorcio',
        on_delete=models.CASCADE,
        related_name='gastos',
    )
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField()
    tipo = models.CharField(
        max_length=15,
        choices=Tipos.choices,
        default=Tipos.ORDINARIO,
    )
    comprobante = models.FileField(upload_to='comprobantes/', null=True, blank=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.descripcion} (${self.monto})'


class Liquidacion(models.Model):
    class Estados(models.TextChoices):
        ABIERTA = 'abierta', 'Abierta'
        CERRADA = 'cerrada', 'Cerrada'

    consorcio = models.ForeignKey(
        'consorcios.Consorcio',
        on_delete=models.CASCADE,
        related_name='liquidaciones',
    )
    mes = models.PositiveSmallIntegerField()   # 1 a 12
    anio = models.PositiveIntegerField()
    estado = models.CharField(
        max_length=10,
        choices=Estados.choices,
        default=Estados.ABIERTA,
    )
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('consorcio', 'anio', 'mes')
        ordering = ['-anio', '-mes']

    def __str__(self):
        return f'{self.consorcio.nombre} - {self.mes:02d}/{self.anio}'

    # ---- Reglas de negocio (calculadas, no guardadas) ----
    @property
    def gastos_periodo(self):
        """Gastos del consorcio correspondientes al mes/año de la liquidacion."""
        return self.consorcio.gastos.filter(fecha__year=self.anio, fecha__month=self.mes)

    @property
    def monto_total(self):
        return sum((g.monto for g in self.gastos_periodo), Decimal('0'))

    def monto_para_unidad(self, unidad):
        """Prorrateo: total del periodo x porcentaje fiscal / 100."""
        return (self.monto_total * unidad.porcentaje_fiscal / Decimal('100')).quantize(Decimal('0.01'))


class Pago(models.Model):
    class Estados(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        CONFIRMADO = 'confirmado', 'Confirmado'

    liquidacion = models.ForeignKey(
        Liquidacion,
        on_delete=models.CASCADE,
        related_name='pagos',
    )
    unidad = models.ForeignKey(
        'consorcios.Unidad',
        on_delete=models.CASCADE,
        related_name='pagos',
    )
    registrado_por = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        related_name='pagos_registrados',
    )
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=Estados.choices,
        default=Estados.PENDIENTE,
    )

    def __str__(self):
        return f'Pago ${self.monto} - {self.unidad} ({self.estado})'