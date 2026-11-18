from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.radicacion.models import Radicacion

from .serializers import RadicacionSerializer


class RadicacionViewSet(ModelViewSet):
    queryset = Radicacion.objects.all()
    serializer_class = RadicacionSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.LIDER]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]
