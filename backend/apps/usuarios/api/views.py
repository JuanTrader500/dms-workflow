from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.core.enums import RolUsuario
from apps.core.permissions import TienePermisoRol
from apps.usuarios.models import Colaborador

from .serializers import ColaboradorSerializer, PerfilSerializer


class ColaboradorViewSet(ReadOnlyModelViewSet):
    """Búsqueda de colaboradores activos (RF-001). Filtro simple ?q= por nombre o identificación."""

    serializer_class = ColaboradorSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [RolUsuario.AUXILIAR_ADMIN_PERSONAL, RolUsuario.LIDER]

    def get_queryset(self):
        qs = Colaborador.objects.filter(activo=True)
        q = self.request.query_params.get("q")
        if q:
            from django.db.models import Q

            qs = qs.filter(Q(nombre__icontains=q) | Q(identificacion__icontains=q))
        return qs


@api_view(["GET"])
def perfil(request):
    return Response(PerfilSerializer(request.user).data)
