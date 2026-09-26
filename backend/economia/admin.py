from django.contrib import admin
from .models import Gasto, Liquidacion, Pago

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', 'monto', 'tipo', 'consorcio')
    list_filter = ('consorcio', 'tipo')
    date_hierarchy = 'fecha'

@admin.register(Liquidacion)
class LiquidacionAdmin(admin.ModelAdmin):
    list_display = ('consorcio', 'mes', 'anio', 'estado', 'monto_total', 'detalle_prorrateo')
    list_filter = ('consorcio', 'anio')

    def detalle_prorrateo(self, obj):
        return ", ".join(
            f"{u.numero}: {obj.monto_para_unidad(u)}"
            for u in obj.consorcio.unidades.all()
        )
    detalle_prorrateo.short_description = "Prorrateo por unidad"


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'liquidacion', 'unidad', 'monto', 'estado')
    list_filter = ('estado',)