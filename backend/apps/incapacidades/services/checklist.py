"""Checklist dinámico y completitud documental (RF-002, RF-004, RN-004)."""

from __future__ import annotations



def generar_checklist(incapacidad) -> None:
    """RF-002: crea ChecklistDocumental e ItemChecklist desde ReglaDocumental del tipo de caso; tipo sin reglas => TipoCasoNoReconocido."""
    raise NotImplementedError("T-10")


def vincular_documento(incapacidad, documento) -> None:
    """RF-003: marca el ítem del tipo como CARGADO y vincula el documento."""
    raise NotImplementedError("T-12")


def validar_completitud(incapacidad, usuario=None) -> list:
    """RF-004: devuelve los ítems faltantes. Completo => caso listo para validación; incompleto => DOC_INCOMPLETA y dispara emisión del aviso 1 (RF-005)."""
    raise NotImplementedError("T-13")
