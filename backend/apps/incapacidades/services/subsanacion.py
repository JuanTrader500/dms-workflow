"""Plazo de subsanación y avisos (RF-005, RN-005, decisión 6)."""

from __future__ import annotations



def emitir_aviso(incapacidad, numero: int) -> None:
    """Crea AvisoSubsanacion con fecha_limite = +3 días hábiles (core.utils.dias_habiles) y notifica por correo + sistema."""
    raise NotImplementedError("T-34")


def procesar_plazos_vencidos(hoy) -> int:
    """Job diario: aviso 1 vencido => aviso 2; aviso 2 vencido => estado PENDIENTE_DECISION_ADMIN + tarea de revisión manual. NO da de baja el caso."""
    raise NotImplementedError("T-34")
