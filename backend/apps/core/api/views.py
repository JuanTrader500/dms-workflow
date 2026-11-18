"""Configuración editable sin redeploy (RNF-008). TODO(T-40): validaciones y auditoría de cambios."""

from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.core.enums import RolUsuario
from apps.core.models import ParametroReconocimiento, ParametroSistema
from apps.core.permissions import TienePermisoRol


class ParametroSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroSistema
        fields = "__all__"


class ParametroReconocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroReconocimiento
        fields = "__all__"


class ParametrosView(ListAPIView):
    queryset = ParametroSistema.objects.all()
    serializer_class = ParametroSistemaSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [RolUsuario.AUXILIAR_ADMIN_PERSONAL]
    roles_escritura = [RolUsuario.AUXILIAR_ADMIN_PERSONAL]  # TODO(T-40): PUT/PATCH


class ReconocimientoConfigView(ListAPIView):
    queryset = ParametroReconocimiento.objects.all()
    serializer_class = ParametroReconocimientoSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [RolUsuario.AUXILIAR_ADMIN_PERSONAL, RolUsuario.LIDER]
    roles_escritura = [RolUsuario.AUXILIAR_ADMIN_PERSONAL]  # TODO(T-40)


@api_view(["GET"])
@permission_classes([AllowAny])
def salud(request):
    return Response({"estado": "ok"})
