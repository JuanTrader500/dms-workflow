"""Control de uso diario de la API gratuita (RNF-007)."""

from __future__ import annotations



def registrar_uso() -> int:
    """Incrementa el contador diario (ParametroSistema o caché). Devuelve el total del día."""
    raise NotImplementedError("T-22")


def limite_excedido() -> bool:
    """True si se alcanzó IA_LIMITE_DIARIO => modo manual con mensaje claro."""
    raise NotImplementedError("T-22")


def estado_ia() -> dict:
    """Para GET /ia/estado/: {proveedor, disponible, usados_hoy, limite}."""
    raise NotImplementedError("T-22")
