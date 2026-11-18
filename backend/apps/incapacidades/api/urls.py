from rest_framework.routers import DefaultRouter

from .views import AlertaViewSet, IncapacidadViewSet, ReglaDocumentalViewSet

router = DefaultRouter()
router.register("incapacidades", IncapacidadViewSet, basename="incapacidad")
router.register("alertas", AlertaViewSet, basename="alerta")
router.register("config/reglas-documentales", ReglaDocumentalViewSet, basename="regla-documental")
urlpatterns = router.urls
