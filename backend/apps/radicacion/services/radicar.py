"""Radicación y respuesta de la entidad (RF-010, RF-011, RN-006, RN-009)."""

from __future__ import annotations



def registrar_radicacion(incapacidad, fecha_radicacion, numero_radicado: str, evidencia, usuario) -> 'Radicacion':
    """RF-010: precondiciones => checklist completo (RF-004) y caso VALIDADA (RF-008); si hay inconsistencia lanza CasoBloqueado (409). Guarda evidencia, cambia estado a TRANSCRITA y audita. Aplica RN-006 para por_correo."""
    raise NotImplementedError("T-28")


def registrar_respuesta_entidad(radicacion, respuesta: str, usuario, causal: str = '') -> None:
    """RF-011: ACEPTADA => COBRADA, PAGADA => PAGADA, RECHAZADA => RECHAZADA con causal (RF-012). Usa estados.cambiar_estado."""
    raise NotImplementedError("T-29")
