from rest_framework.routers import DefaultRouter

from .views import RadicacionViewSet

router = DefaultRouter()
router.register("radicaciones", RadicacionViewSet, basename="radicacion")
urlpatterns = router.urls
