"""Resolución de discrepancias bloqueadas (RF-008, decisión 11)."""

from __future__ import annotations



def resolver_discrepancia(datos_extraidos, accion: str, valores: dict, usuario) -> None:
    """Solo AUXILIAR_ADMIN_PERSONAL. accion='corregir_registro' (actualiza la Incapacidad) o 'marcar_extraido_erroneo'. Ambas exigen confirmación explícita, marcan CONFIRMADO_MANUAL, liberan el bloqueo si no quedan otras discrepancias y auditan."""
    raise NotImplementedError("T-21")
