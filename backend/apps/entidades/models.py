"""EntidadEPSARL y tabla de SLA de transcripción (RF-009, RN-006, RN-007). Configuración editable (RNF-008)."""

from django.db import models

from apps.core.enums import TipoCaso, TipoEntidad
from apps.core.models import ModeloBase


class EntidadEPSARL(ModeloBase):
    nombre = models.CharField(max_length=120, unique=True)
    tipo = models.CharField(max_length=3, choices=TipoEntidad.choices, default=TipoEntidad.EPS)
    transcripcion_por_correo = models.BooleanField(
        default=False, help_text="RN-006: SOS, Sanitas y Famisanar transcriben por correo"
    )

    def __str__(self):
        return self.nombre


class PlazoTranscripcion(ModeloBase):
    """Plazo en días calendario. tipo_caso vacío = aplica a todos los tipos de la entidad."""

    entidad = models.ForeignKey(EntidadEPSARL, on_delete=models.CASCADE, related_name="plazos")
    tipo_caso = models.CharField(max_length=30, choices=TipoCaso.choices, null=True, blank=True)
    plazo_dias = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["entidad", "tipo_caso"], name="uq_plazo_entidad_tipo"),
        ]
