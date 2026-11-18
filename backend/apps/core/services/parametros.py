"""Acceso tipado a ParametroSistema con caché corta (efecto ≤ 5 min, RNF-008)."""

from __future__ import annotations



def obtener_float(clave: str, defecto: float) -> float:
    """Lee un parámetro numérico; usa `defecto` si no existe."""
    raise NotImplementedError("T-05")


def obtener_int(clave: str, defecto: int) -> int:
    """Lee un parámetro entero."""
    raise NotImplementedError("T-05")


def obtener_lista_int(clave: str, defecto: list[int]) -> list[int]:
    """Lee una lista separada por comas (p. ej. UMBRALES_DIAS)."""
    raise NotImplementedError("T-05")


def festivos() -> set:
    """Conjunto de fechas festivas para días hábiles."""
    raise NotImplementedError("T-05")
