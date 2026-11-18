from rest_framework.viewsets import ModelViewSet

from apps.core.enums import RolUsuario
from apps.core.permissions import TienePermisoRol
from apps.entidades.models import EntidadEPSARL, PlazoTranscripcion

from .serializers import EntidadSerializer, PlazoTranscripcionSerializer

LECTURA = [RolUsuario.AUXILIAR_ADMIN_PERSONAL, RolUsuario.LIDER, RolUsuario.CONTABILIDAD]
ESCRITURA = [RolUsuario.AUXILIAR_ADMIN_PERSONAL]


class EntidadViewSet(ModelViewSet):
    queryset = EntidadEPSARL.objects.all()
    serializer_class = EntidadSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura, roles_escritura = LECTURA, ESCRITURA


class PlazoTranscripcionViewSet(ModelViewSet):
    """Configuración de plazos sin redeploy (RNF-008)."""

    queryset = PlazoTranscripcion.objects.select_related("entidad")
    serializer_class = PlazoTranscripcionSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura, roles_escritura = ESCRITURA, ESCRITURA
