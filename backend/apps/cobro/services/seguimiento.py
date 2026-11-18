"""Seguimiento semanal de cobro (RF-016, RN-010)."""

from __future__ import annotations



def registrar_seguimiento(incapacidad, estado: str, saldo, evidencia, usuario) -> 'SeguimientoCobro':
    """RF-016: añade registro con fecha, estado y saldo; marca plazo máximo vencido si > 3 años desde la transcripción sin pago (RN-010)."""
    raise NotImplementedError("T-37")
