"""Escalamiento a Cartera y Jurídica (RF-019, RF-020, RN-015). POST-MVP."""

from __future__ import annotations



def escalar_a_cartera(hoy) -> int:
    """RF-019: 180 días desde el primer requerimiento sin pago (o deterioro crediticio manual) => crea EscalamientoCartera, cambia responsable_actual y notifica. Idempotente."""
    raise NotImplementedError("T-46")


def escalar_a_juridica(escalamiento, usuario) -> None:
    """RF-020: Cartera marca gestión agotada => crea GestionJuridica."""
    raise NotImplementedError("T-46")


def registrar_decision_final(gestion, decision: str, usuario) -> None:
    """RF-020: recuperar o dar de baja; cierra el ciclo de cobro."""
    raise NotImplementedError("T-46")
