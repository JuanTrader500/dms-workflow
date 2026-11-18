from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.auditoria.models import AuditoriaGestion

from .serializers import AuditoriaGestionSerializer


class AuditoriaGestionViewSet(ReadOnlyModelViewSet):
    queryset = AuditoriaGestion.objects.all()
    serializer_class = AuditoriaGestionSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.LIDER, R.CARTERA, R.JURIDICA, R.GESTION_DOCUMENTAL]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]
