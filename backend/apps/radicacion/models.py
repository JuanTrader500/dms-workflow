"""Radicacion (RF-010, RF-011, RF-012)."""

from django.db import models

from apps.core.models import ModeloBase


def ruta_evidencia(instancia, nombre):
    return f"radicaciones/{instancia.incapacidad_id}/{nombre}"


class Radicacion(ModeloBase):
    incapacidad = models.ForeignKey("incapacidades.Incapacidad", on_delete=models.CASCADE, related_name="radicaciones")
    fecha_radicacion = models.DateField()
    numero_radicado = models.CharField(max_length=60, blank=True)
    evidencia = models.FileField(upload_to=ruta_evidencia, null=True, blank=True)
    por_correo = models.BooleanField(default=False, help_text="RN-006: SOS/Sanitas/Famisanar")
    respuesta_entidad = models.CharField(max_length=20, blank=True, help_text="ACEPTADA | RECHAZADA | PAGADA")
    causal_rechazo = models.TextField(blank=True)
    fecha_respuesta = models.DateField(null=True, blank=True)
    registrado_por = models.ForeignKey("usuarios.Usuario", null=True, blank=True, on_delete=models.SET_NULL)
