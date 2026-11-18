"""Alertas de plazo y umbrales (RF-013, RF-014, RN-007, RN-014)."""

from __future__ import annotations



def generar_alertas_transcripcion(hoy) -> int:
    """RF-013: casos con fecha_limite_transcripcion en la ventana DIAS_ALERTA_PREVIA_TRANSCRIPCION y sin transcribir. Idempotente."""
    raise NotImplementedError("T-31")


def generar_alertas_umbral(hoy) -> int:
    """RF-014: días transcurridos == 90/120/150/180 => AlertaPlazo (get_or_create). Registra para el reporte mensual."""
    raise NotImplementedError("T-36")
