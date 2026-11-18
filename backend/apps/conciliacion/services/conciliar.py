"""Apoyo a la conciliación con Contabilidad/Tesorería (RF-022, RN-012)."""

from __future__ import annotations



def cruzar_pagos(periodo: str, valores_consignados: list[dict], usuario) -> 'ConciliacionContable':
    """RF-022: cruza valores consignados con casos PAGADA por colaborador/entidad/periodo; los no identificables => pendiente_identificar y notificación a Contabilidad."""
    raise NotImplementedError("T-39")
