from rest_framework.routers import DefaultRouter

from .views import ReporteAusentismoViewSet

router = DefaultRouter()
router.register("reportes-ausentismo", ReporteAusentismoViewSet, basename="reporte-ausentismo")
urlpatterns = router.urls
