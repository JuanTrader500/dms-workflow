from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.core.enums import RolUsuario as R
from apps.core.permissions import TienePermisoRol
from apps.cobro.models import SeguimientoCobro, ReconocimientoEconomico, RequerimientoCobro, EscalamientoCartera, GestionJuridica

from .serializers import SeguimientoCobroSerializer, ReconocimientoEconomicoSerializer, RequerimientoCobroSerializer, EscalamientoCarteraSerializer, GestionJuridicaSerializer


class SeguimientoCobroViewSet(ModelViewSet):
    queryset = SeguimientoCobro.objects.all()
    serializer_class = SeguimientoCobroSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]


class ReconocimientoEconomicoViewSet(ReadOnlyModelViewSet):
    queryset = ReconocimientoEconomico.objects.all()
    serializer_class = ReconocimientoEconomicoSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.LIDER]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL]


class RequerimientoCobroViewSet(ModelViewSet):
    queryset = RequerimientoCobro.objects.all()
    serializer_class = RequerimientoCobroSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.CARTERA, R.JURIDICA]
    roles_escritura = [R.AUXILIAR_ADMIN_PERSONAL, R.CARTERA, R.JURIDICA]


class EscalamientoCarteraViewSet(ModelViewSet):
    queryset = EscalamientoCartera.objects.all()
    serializer_class = EscalamientoCarteraSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.CARTERA, R.JURIDICA]
    roles_escritura = [R.CARTERA, R.JURIDICA]


class GestionJuridicaViewSet(ModelViewSet):
    queryset = GestionJuridica.objects.all()
    serializer_class = GestionJuridicaSerializer
    permission_classes = [TienePermisoRol]
    roles_lectura = [R.AUXILIAR_ADMIN_PERSONAL, R.CARTERA, R.JURIDICA]
    roles_escritura = [R.JURIDICA]
