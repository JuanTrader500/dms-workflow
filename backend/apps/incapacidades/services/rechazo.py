"""Rechazo y resubsanación (RF-012, RN-009)."""

from __future__ import annotations



def registrar_rechazo(incapacidad, causal: str, usuario) -> None:
    """RF-012: estado RECHAZADA y causal conservada en el historial."""
    raise NotImplementedError("T-35")


def resubsanar(incapacidad, usuario) -> None:
    """RF-012: vuelve a DOC_INCOMPLETA o VALIDADA según el motivo; conserva historial."""
    raise NotImplementedError("T-35")
