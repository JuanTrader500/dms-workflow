"""Punto único de registro de auditoría (RF-024). Toda escritura sobre un caso debe pasar por aquí."""

from __future__ import annotations


def registrar(*, usuario=None, accion: str, incapacidad=None, detalle: dict | None = None):
    """Crea una entrada inmutable. `usuario=None` equivale a 'Sistema'. NUNCA incluir contenido clínico en `detalle`."""
    from apps.auditoria.models import AuditoriaGestion

    return AuditoriaGestion.objects.create(
        usuario=usuario if getattr(usuario, "pk", None) else None,
        incapacidad=incapacidad,
        accion=accion,
        detalle=detalle or {},
    )
