"""Cálculo de días hábiles (RN-005: plazo de subsanación de 3 días hábiles).

Función pura, sin dependencias de Django, fácil de probar.
Los festivos se pasan como conjunto; el servicio los toma de core.Festivo.
"""

from __future__ import annotations

from datetime import date, timedelta


def es_habil(dia: date, festivos: frozenset[date] | set[date] = frozenset()) -> bool:
    return dia.weekday() < 5 and dia not in festivos


def sumar_dias_habiles(inicio: date, cantidad: int, festivos: frozenset[date] | set[date] = frozenset()) -> date:
    """Devuelve la fecha resultante de sumar `cantidad` días hábiles a `inicio` (excluyéndolo)."""
    if cantidad < 0:
        raise ValueError("La cantidad de días hábiles no puede ser negativa.")
    actual = inicio
    restantes = cantidad
    while restantes > 0:
        actual += timedelta(days=1)
        if es_habil(actual, festivos):
            restantes -= 1
    return actual
