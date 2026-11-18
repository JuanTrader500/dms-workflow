"""Registro del caso (RF-001, RN-001..RN-003)."""

from __future__ import annotations



def registrar_incapacidad(*, colaborador_id: int, tipo_caso: str, fecha_inicio, canal: str, fecha_expedicion=None, fecha_remision=None, usuario=None):
    """RF-001: valida colaborador activo (ColaboradorNoEncontrado), calcula remision_tardia (RN-003, no bloqueante), crea Incapacidad en REGISTRADA, genera checklist (RF-002) y audita. Todo en una transacción."""
    raise NotImplementedError("T-10")
