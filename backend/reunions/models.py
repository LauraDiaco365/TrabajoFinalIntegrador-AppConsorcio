from django.db import models

class Reunion(models.Model):
    class Estados(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        FINALIZADA = 'finalizada', 'Finalizada'
        CANCELADA = 'cancelada', 'Cancelada'

    consorcio = models.ForeignKey('consorcios.Consorcio', on_delete=models.CASCADE, related_name='reuniones')
    titulo = models.CharField(max_length=200)
    temario = models.TextField()
    fecha_hora = models.DateTimeField()
    lugar_o_enlace = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=Estados.choices, default=Estados.PENDIENTE)

    def __str__(self):
        return f"{self.titulo} - {self.consorcio.nombre}"