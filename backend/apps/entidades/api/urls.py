from rest_framework.routers import DefaultRouter

from .views import EntidadViewSet, PlazoTranscripcionViewSet

router = DefaultRouter()
router.register("entidades", EntidadViewSet, basename="entidad")
router.register("config/plazos", PlazoTranscripcionViewSet, basename="plazo-transcripcion")
urlpatterns = router.urls
