"""Carga, validación y destrucción de documentos (RF-003, RF-006, RF-023, RN-016)."""

from __future__ import annotations



def validar_archivo(archivo) -> str:
    """RF-003: valida tamaño (MAX_UPLOAD_MB) y MIME real con `filetype` (no solo la extensión). Solo PDF/JPG/PNG; si no, DocumentoInvalido. Devuelve el MIME."""
    raise NotImplementedError("T-12")


def guardar_documento(incapacidad, archivo, tipo_documento: str, usuario) -> 'DocumentoSoporte':
    """RF-003/RF-006: valida, calcula SHA-256, almacena, etiqueta el tipo, vincula al ítem del checklist y audita."""
    raise NotImplementedError("T-12")


def etiquetar_tipo(documento, tipo_documento: str, usuario) -> None:
    """RF-006: cambia el tipo (selecciona el esquema de extracción) y audita."""
    raise NotImplementedError("T-19")


def destruir_documentos_clinicos(incapacidad, usuario) -> int:
    """RF-023/RN-016: borra del almacenamiento de forma NO recuperable los archivos clínicos (sobrescritura + unlink), marca destruido=True. Post-MVP."""
    raise NotImplementedError("T-47")
