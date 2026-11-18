"""ReporteAusentismo (RF-021, RN-017)."""

from django.db import models

from apps.core.models import ModeloBase


class ReporteAusentismo(ModeloBase):
    periodo = models.CharField(max_length=7, unique=True, help_text="AAAA-MM del mes reportado")
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    archivo = models.FileField(upload_to="reportes/", null=True, blank=True)
    enviado_sgsst = models.BooleanField(default=False)
    incapacidades = models.ManyToManyField("incapacidades.Incapacidad", blank=True, related_name="reportes_ausentismo")
