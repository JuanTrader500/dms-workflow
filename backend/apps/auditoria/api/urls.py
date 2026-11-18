from rest_framework.routers import DefaultRouter

from .views import AuditoriaGestionViewSet

router = DefaultRouter()
router.register("auditoria", AuditoriaGestionViewSet, basename="auditoria")
urlpatterns = router.urls
