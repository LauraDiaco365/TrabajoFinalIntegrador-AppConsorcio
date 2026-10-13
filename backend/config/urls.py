from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# 1. Importamos las vistas de ambas aplicaciones
from consorcios.views import ConsorcioViewSet, UnidadViewSet
from economia.views import GastoViewSet, LiquidacionViewSet, PagoViewSet

# 2. Creamos un ÚNICO enrutador para toda la API
router = DefaultRouter()

# 3. Registramos TODAS las rutas en este enrutador
router.register(r'consorcios', ConsorcioViewSet)
router.register(r'unidades', UnidadViewSet)
router.register(r'gastos', GastoViewSet)
router.register(r'liquidaciones', LiquidacionViewSet)
router.register(r'pagos', PagoViewSet)

# 4. Definimos las URLs finales
urlpatterns = [
    path('admin/', admin.site.urls),
    # Conectamos nuestro enrutador unificado a la ruta 'api/'
    path('api/', include(router.urls)),
]