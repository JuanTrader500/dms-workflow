"""RF-024 / RNF-005 / CA-08."""

import pytest

from apps.auditoria.models import AuditoriaGestion, AuditoriaInmutableError
from apps.auditoria.services.registrar import registrar


@pytest.mark.django_db
def test_no_se_puede_editar_ni_borrar():
    entrada = registrar(accion="PRUEBA", detalle={"x": 1})
    entrada.accion = "OTRA"
    with pytest.raises(AuditoriaInmutableError):
        entrada.save()
    with pytest.raises(AuditoriaInmutableError):
        entrada.delete()
    with pytest.raises(AuditoriaInmutableError):
        AuditoriaGestion.objects.all().update(accion="X")
    with pytest.raises(AuditoriaInmutableError):
        AuditoriaGestion.objects.all().delete()
