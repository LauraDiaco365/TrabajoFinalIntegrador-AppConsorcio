from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsorcioViewSet, UnidadViewSet

router = DefaultRouter()
# Esto creará las rutas /consorcios/ y /consorcios/<id>/
router.register(r'consorcios', ConsorcioViewSet)
# Esto creará las rutas /unidades/ y /unidades/<id>/
router.register(r'unidades', UnidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]