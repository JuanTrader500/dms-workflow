from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.conciliacion.models import ConciliacionContable

from .serializers import ConciliacionContableSerializer


class ConciliacionContableViewSet(ModelViewSet):
    queryset = ConciliacionContable.objects.all()
    serializer_class = ConciliacionContableSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.CONTABILIDAD]
    roles_escritura = [R.CONTABILIDAD]
