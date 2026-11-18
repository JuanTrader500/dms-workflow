"""Notificación dual: en sistema + correo (decisión 8)."""

from django.conf import settings
from django.db import models

from apps.core.models import ModeloBase


class Notificacion(ModeloBase):
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notificaciones")
    incapacidad = models.ForeignKey("incapacidades.Incapacidad", null=True, blank=True, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=300)
    leida = models.BooleanField(default=False)
    correo_enviado = models.BooleanField(default=False)
    intentos_correo = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["-creado_en"]
