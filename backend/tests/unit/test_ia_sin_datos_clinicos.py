"""RNF-001 / CA-03 / T-24: ni el modelo ni el esquema pueden contener campos clínicos."""

from apps.ia.models import DatosExtraidos
from apps.ia.schemas import ExtraccionCertificadoIncapacidad

PROHIBIDOS = ("diagnostico", "cie", "cie10", "clinic", "epicrisis", "medico", "tratamiento")


def _limpios(nombres):
    return [n for n in nombres if any(p in n.lower() for p in PROHIBIDOS)]


def test_modelo_sin_campos_clinicos():
    assert _limpios(f.name for f in DatosExtraidos._meta.get_fields()) == []


def test_esquema_sin_campos_clinicos():
    assert _limpios(ExtraccionCertificadoIncapacidad.model_fields) == []
