from django.db import models

class Mantenimiento(models.Model):
    class Estados(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        EN_PROCESO = 'en_proceso', 'En Proceso'
        FINALIZADO = 'finalizado', 'Finalizado'

    consorcio = models.ForeignKey('consorcios.Consorcio', on_delete=models.CASCADE, related_name='mantenimientos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=Estados.choices, default=Estados.PENDIENTE)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"