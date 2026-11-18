"""RF-011 / RN-009: máquina de estados."""

import pytest

from apps.core.enums import EstadoCaso as E
from apps.core.exceptions import TransicionInvalida
from apps.incapacidades.services.estados import es_transicion_valida, validar_transicion


def test_camino_feliz():
    camino = [E.REGISTRADA, E.VALIDADA, E.TRANSCRITA, E.COBRADA, E.PAGADA, E.ARCHIVADA]
    for origen, destino in zip(camino, camino[1:]):
        assert es_transicion_valida(origen, destino)


def test_no_se_puede_radicar_sin_validar():
    with pytest.raises(TransicionInvalida):
        validar_transicion(E.REGISTRADA, E.TRANSCRITA)


def test_inconsistencia_solo_sale_a_validada():
    assert es_transicion_valida(E.EN_REVISION_INCONSISTENCIA, E.VALIDADA)
    assert not es_transicion_valida(E.EN_REVISION_INCONSISTENCIA, E.TRANSCRITA)


def test_archivada_es_terminal():
    assert not any(es_transicion_valida(E.ARCHIVADA, e) for e in E)
