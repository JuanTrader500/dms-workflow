"""DatosExtraidos (RF-007/008). SIN columnas clínicas: minimización de datos (RNF-001).

Un test (T-24) recorre `DatosExtraidos._meta` y falla si aparece un campo de diagnóstico/CIE.
"""

from django.db import models

from apps.core.enums import EstadoValidacion
from apps.core.models import ModeloBase


class DatosExtraidos(ModeloBase):
    documento = models.OneToOneField("documentos.DocumentoSoporte", on_delete=models.CASCADE, related_name="datos_extraidos")
    nombre_colaborador = models.CharField(max_length=150, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    dias_incapacidad = models.PositiveIntegerField(null=True, blank=True)
    entidad_emisora = models.CharField(max_length=120, blank=True, null=True)
    confianza = models.FloatField(default=0.0)
    estado = models.CharField(max_length=20, choices=EstadoValidacion.choices, default=EstadoValidacion.PENDIENTE)
    discrepancias = models.JSONField(default=list, blank=True, help_text="Solo nombres de campos operativos y valores comparados")
    confirmado_por = models.ForeignKey("usuarios.Usuario", null=True, blank=True, on_delete=models.SET_NULL)
    confirmado_en = models.DateTimeField(null=True, blank=True)

    def requiere_revision_manual(self) -> bool:
        return self.estado in {EstadoValidacion.EN_REVISION, EstadoValidacion.VERIFICACION_MANUAL}
