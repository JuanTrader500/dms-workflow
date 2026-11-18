from rest_framework.routers import DefaultRouter

from .views import ConciliacionContableViewSet

router = DefaultRouter()
router.register("conciliaciones", ConciliacionContableViewSet, basename="conciliacion")
urlpatterns = router.urls
