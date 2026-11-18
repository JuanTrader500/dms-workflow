"""Concepto de rehabilitación (RF-015, RN-014)."""

from __future__ import annotations



def registrar_concepto(incapacidad, fecha_emision, resultado, usuario) -> None:
    """RF-015: registra el concepto; si es antes del día 150, deja constancia de remisión al AFP."""
    raise NotImplementedError("T-36")


def notificar_incumplimiento(incapacidad) -> None:
    """RF-015: sin concepto al día 150 => notificar EPS, ARL, AFP y trabajador."""
    raise NotImplementedError("T-36")
