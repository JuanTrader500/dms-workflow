"""Envío de notificaciones con canal dual y reintentos (RNF-002, decisión 8)."""

from __future__ import annotations



def notificar(destinatarios, mensaje: str, incapacidad=None, asunto: str = 'DMS Workflow') -> int:
    """Crea Notificacion en sistema y envía correo; hasta 3 reintentos con backoff ante fallo del canal (RNF-002). Un fallo de correo no debe perder la notificación en sistema."""
    raise NotImplementedError("T-31")
