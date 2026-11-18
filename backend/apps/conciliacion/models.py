"""ConciliacionContable (RF-022, RN-012)."""

from django.db import models

from apps.core.models import ModeloBase


class ConciliacionContable(ModeloBase):
    periodo = models.CharField(max_length=7, help_text="AAAA-MM")
    entidad = models.ForeignKey("entidades.EntidadEPSARL", null=True, blank=True, on_delete=models.PROTECT)
    valor_consignado = models.DecimalField(max_digits=14, decimal_places=2)
    identificado = models.BooleanField(default=False)
    pendiente_identificar = models.BooleanField(default=False)
    incapacidades = models.ManyToManyField("incapacidades.Incapacidad", blank=True, related_name="conciliaciones")
