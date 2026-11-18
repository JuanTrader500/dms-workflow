"""DocumentoSoporte (RF-003, RF-006, RF-023)."""

import uuid
from pathlib import Path

from django.db import models

from apps.core.enums import DOCUMENTOS_CLINICOS, TipoDocumento
from apps.core.models import ModeloBase


def ruta_documento(instancia, nombre_original: str) -> str:
    extension = Path(nombre_original).suffix.lower()
    return f"incapacidades/{instancia.incapacidad_id}/{uuid.uuid4().hex}{extension}"


class DocumentoSoporte(ModeloBase):
    incapacidad = models.ForeignKey("incapacidades.Incapacidad", on_delete=models.CASCADE, related_name="documentos")
    archivo = models.FileField(upload_to=ruta_documento, null=True, blank=True)
    nombre_archivo = models.CharField(max_length=255)
    formato = models.CharField(max_length=50, help_text="MIME real detectado")
    tipo_documento = models.CharField(max_length=30, choices=TipoDocumento.choices, default=TipoDocumento.OTRO)
    es_clinico = models.BooleanField(default=False)
    hash_sha256 = models.CharField(max_length=64, blank=True)
    destruido = models.BooleanField(default=False)
    fecha_destruccion = models.DateTimeField(null=True, blank=True)
    cargado_por = models.ForeignKey("usuarios.Usuario", null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.es_clinico = self.tipo_documento in DOCUMENTOS_CLINICOS
        super().save(*args, **kwargs)
