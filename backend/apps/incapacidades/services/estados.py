"""Máquina de estados del caso (RF-011, RN-009). ÚNICO lugar donde cambia `Incapacidad.estado`.

La tabla TRANSICIONES es pura (sin Django) para poder probarla sin base de datos.
"""

from __future__ import annotations

from apps.core.enums import EstadoCaso as E
from apps.core.exceptions import TransicionInvalida

TRANSICIONES: dict[str, frozenset[str]] = {
    E.REGISTRADA: frozenset({E.DOC_INCOMPLETA, E.EN_REVISION_INCONSISTENCIA, E.VALIDADA}),
    E.DOC_INCOMPLETA: frozenset(
        {E.REGISTRADA, E.EN_REVISION_INCONSISTENCIA, E.VALIDADA, E.PENDIENTE_DECISION_ADMIN}
    ),
    E.PENDIENTE_DECISION_ADMIN: frozenset({E.REGISTRADA, E.DOC_INCOMPLETA}),
    E.EN_REVISION_INCONSISTENCIA: frozenset({E.VALIDADA}),
    E.VALIDADA: frozenset({E.TRANSCRITA, E.EN_REVISION_INCONSISTENCIA}),
    E.TRANSCRITA: frozenset({E.COBRADA, E.RECHAZADA}),
    E.COBRADA: frozenset({E.PAGADA}),
    E.RECHAZADA: frozenset({E.DOC_INCOMPLETA, E.VALIDADA}),
    E.PAGADA: frozenset({E.ARCHIVADA}),
    E.ARCHIVADA: frozenset(),
}


def es_transicion_valida(origen: str, destino: str) -> bool:
    return destino in TRANSICIONES.get(origen, frozenset())


def validar_transicion(origen: str, destino: str) -> None:
    if not es_transicion_valida(origen, destino):
        raise TransicionInvalida(f"No se puede pasar de {origen} a {destino}.")


def cambiar_estado(incapacidad, nuevo_estado: str, usuario=None, motivo: str = "") -> None:
    """Valida la transición, persiste y audita (RF-024)."""
    from apps.auditoria.services.registrar import registrar

    anterior = incapacidad.estado
    validar_transicion(anterior, nuevo_estado)
    incapacidad.estado = nuevo_estado
    incapacidad.save(update_fields=["estado", "actualizado_en"])
    registrar(
        usuario=usuario,
        incapacidad=incapacidad,
        accion="CAMBIO_ESTADO",
        detalle={"de": anterior, "a": nuevo_estado, "motivo": motivo},
    )
