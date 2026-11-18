from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.documentos.models import DocumentoSoporte

from .serializers import DocumentoSerializer


class DocumentoViewSet(ModelViewSet):
    queryset = DocumentoSoporte.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.GESTION_DOCUMENTAL]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL, R.COLABORADOR]
    http_method_names = ["get", "post", "patch", "head", "options"]

    def create(self, request, *args, **kwargs):
        """RF-003 + RF-006 (multipart: archivo, incapacidad, tipo_documento). TODO(T-12)."""
        return Response({"detalle": "Pendiente de implementar (T-12)"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=True, methods=["post"], url_path="extraer")
    def extraer(self, request, pk=None):
        """RF-007. TODO(T-18): llamar a apps.ia.services.extraccion.extraer_datos."""
        return Response({"detalle": "Pendiente de implementar (T-18)"}, status=status.HTTP_501_NOT_IMPLEMENTED)
