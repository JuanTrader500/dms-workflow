from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DatosExtraidosViewSet, estado_ia

router = DefaultRouter()
router.register("datos-extraidos", DatosExtraidosViewSet, basename="datos-extraidos")
urlpatterns = router.urls + [path("ia/estado/", estado_ia, name="ia-estado")]
