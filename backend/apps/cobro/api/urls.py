from rest_framework.routers import DefaultRouter

from .views import SeguimientoCobroViewSet, ReconocimientoEconomicoViewSet, RequerimientoCobroViewSet, EscalamientoCarteraViewSet, GestionJuridicaViewSet

router = DefaultRouter()
router.register("seguimientos-cobro", SeguimientoCobroViewSet, basename="seguimiento-cobro")
router.register("reconocimientos", ReconocimientoEconomicoViewSet, basename="reconocimiento")
router.register("requerimientos-cobro", RequerimientoCobroViewSet, basename="requerimiento-cobro")
router.register("escalamientos-cartera", EscalamientoCarteraViewSet, basename="escalamiento-cartera")
router.register("gestiones-juridicas", GestionJuridicaViewSet, basename="gestion-juridica")
urlpatterns = router.urls
