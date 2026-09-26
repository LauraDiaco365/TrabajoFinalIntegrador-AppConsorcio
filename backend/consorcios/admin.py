
from django.contrib import admin
from .models import Consorcio, Unidad

class UnidadInline(admin.TabularInline):
    model = Unidad
    extra = 1

@admin.register(Consorcio)
class ConsorcioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'cuit')
    inlines = [UnidadInline]

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('numero', 'consorcio', 'propietario', 'porcentaje_fiscal')
    list_filter = ('consorcio',)