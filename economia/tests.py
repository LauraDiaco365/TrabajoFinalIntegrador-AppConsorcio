from decimal import Decimal
from django.test import TestCase
from usuarios.models import Usuario
from consorcios.models import Consorcio, Unidad
from economia.models import Gasto, Liquidacion


class ProrrateoTests(TestCase):
    def setUp(self):
        admin = Usuario.objects.create_user(username='admin', password='x', rol='administrador')
        self.consorcio = Consorcio.objects.create(
            nombre='Edificio Test', direccion='Calle Falsa 123', cuit='30-11111111-1',
            administrador=admin,
        )
        # Dos unidades 50/50
        self.u1 = Unidad.objects.create(consorcio=self.consorcio, numero='1A', porcentaje_fiscal=50)
        self.u2 = Unidad.objects.create(consorcio=self.consorcio, numero='1B', porcentaje_fiscal=50)
        # Gasto de $10.000 en agosto 2026
        Gasto.objects.create(consorcio=self.consorcio, descripcion='Luz', monto=10000, fecha='2026-08-10')

    def test_prorrateo_5050(self):
        liq = Liquidacion.objects.create(consorcio=self.consorcio, mes=8, anio=2026)
        self.assertEqual(liq.monto_total, Decimal('10000'))
        self.assertEqual(liq.monto_para_unidad(self.u1), Decimal('5000.00'))
        self.assertEqual(liq.monto_para_unidad(self.u2), Decimal('5000.00'))