from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.reportes.models import ReporteAusentismo

from .serializers import ReporteAusentismoSerializer


class ReporteAusentismoViewSet(ModelViewSet):
    queryset = ReporteAusentismo.objects.all()
    serializer_class = ReporteAusentismoSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]
