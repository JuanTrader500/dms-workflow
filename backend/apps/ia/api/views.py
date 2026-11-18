from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.ia.models import DatosExtraidos

from .serializers import DatosExtraidosSerializer


class DatosExtraidosViewSet(ReadOnlyModelViewSet):
    queryset = DatosExtraidos.objects.select_related("documento").all()
    serializer_class = DatosExtraidosSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]

    @action(detail=True, methods=["post"], url_path="resolver-discrepancia")
    def resolver_discrepancia(self, request, pk=None):
        """RF-008. TODO(T-21): {accion: corregir_registro|marcar_extraido_erroneo, valores:{...}}."""
        return Response({"detalle": "Pendiente de implementar (T-21)"}, status=status.HTTP_501_NOT_IMPLEMENTED)


class _EstadoIAPermiso(TienePermisoRol):
    pass


@api_view(["GET"])
@permission_classes([_EstadoIAPermiso])
def estado_ia(request):
    """RNF-007. TODO(T-22): usar services.uso.estado_ia()."""
    from django.conf import settings

    return Response({"proveedor": settings.IA_PROVEEDOR, "modelo": settings.GEMINI_MODEL})


estado_ia.cls.roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL]
