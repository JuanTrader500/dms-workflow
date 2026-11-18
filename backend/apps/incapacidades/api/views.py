from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.incapacidades.models import AlertaPlazo, Incapacidad, ReglaDocumental

from .serializers import (
    AlertaSerializer,
    IncapacidadCrearSerializer,
    IncapacidadSerializer,
    ReglaDocumentalSerializer,
)


class IncapacidadViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    """Listado/detalle (RF-001..004). La creación pasa por el servicio `registrar_incapacidad`."""

    queryset = Incapacidad.objects.select_related("colaborador", "entidad", "checklist").all()
    serializer_class = IncapacidadSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.LIDER, R.CARTERA, R.JURIDICA, R.COLABORADOR]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]
    filterset_fields = ["estado", "entidad", "tipo_caso"]

    def get_queryset(self):
        qs = super().get_queryset()
        for campo in ("estado", "entidad", "tipo_caso"):
            valor = self.request.query_params.get(campo)
            if valor:
                qs = qs.filter(**{campo: valor})
        return qs

    def create(self, request):
        """RF-001. TODO(T-10): conectar con services.registro.registrar_incapacidad."""
        entrada = IncapacidadCrearSerializer(data=request.data)
        entrada.is_valid(raise_exception=True)
        # incapacidad = registrar_incapacidad(**entrada.validated_data, usuario=request.user)
        return Response({"detalle": "Pendiente de implementar (T-10)"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=True, methods=["post"], url_path="validar-completitud")
    def validar_completitud(self, request, pk=None):
        """RF-004. TODO(T-13)."""
        return Response({"detalle": "Pendiente de implementar (T-13)"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=True, methods=["post"], url_path="asociar-entidad")
    def asociar_entidad(self, request, pk=None):
        """RF-009. TODO(T-26)."""
        return Response({"detalle": "Pendiente de implementar (T-26)"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=True, methods=["post"], url_path="transicion")
    def transicion(self, request, pk=None):
        """RF-011. TODO(T-27): usar services.estados.cambiar_estado."""
        return Response({"detalle": "Pendiente de implementar (T-27)"}, status=status.HTTP_501_NOT_IMPLEMENTED)


# Nota: el método de escritura POST se autoriza con roles_escritura, aunque create() sea manual.


class AlertaViewSet(ModelViewSet):
    queryset = AlertaPlazo.objects.select_related("incapacidad").all()
    serializer_class = AlertaSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]
    http_method_names = ["get", "patch", "head", "options"]


class ReglaDocumentalViewSet(ModelViewSet):
    queryset = ReglaDocumental.objects.all()
    serializer_class = ReglaDocumentalSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]
