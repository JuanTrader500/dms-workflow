"""Asociación de entidad y cálculo del plazo de transcripción (RF-009, RN-006, RN-007)."""

from __future__ import annotations



def calcular_fecha_limite(incapacidad) -> 'date':
    """RF-009/RN-007: busca PlazoTranscripcion (entidad+tipo_caso, luego entidad sin tipo). Si no hay, lanza PlazoNoParametrizado. fecha_limite = fecha_inicio + plazo_dias."""
    raise NotImplementedError("T-26")


def asociar_entidad(incapacidad, entidad, usuario) -> None:
    """RF-009: asigna la entidad, calcula y guarda fecha_limite_transcripcion y registra auditoría."""
    raise NotImplementedError("T-26")


def canal_transcripcion(entidad) -> str:
    """RN-006: devuelve 'CORREO' o 'PORTAL' según la entidad."""
    raise NotImplementedError("T-26")
