"""Reporte mensual de ausentismo para SG-SST (RF-021, RN-017)."""

from __future__ import annotations



def generar_reporte(periodo: str, usuario=None) -> 'ReporteAusentismo':
    """RF-021: casos activos/cerrados del mes; exporta CSV (y PDF opcional) al almacenamiento."""
    raise NotImplementedError("T-38")


def enviar_a_sgsst(reporte) -> None:
    """RF-021: envía por correo al SG-SST; marca enviado_sgsst."""
    raise NotImplementedError("T-38")
