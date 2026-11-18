"""Modelos base y de configuración editable (RNF-008)."""

from django.db import models

from .enums import ResponsablePago


class ModeloBase(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ParametroSistema(ModeloBase):
    """Parámetros editables sin redeploy (umbral de IA, plazos, antelaciones)."""

    clave = models.CharField(max_length=80, unique=True)
    valor = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.clave}={self.valor}"


class ParametroReconocimiento(ModeloBase):
    """Tramos del reconocimiento económico (RN-013, RF-017). Editable."""

    dia_desde = models.PositiveIntegerField()
    dia_hasta = models.PositiveIntegerField(null=True, blank=True, help_text="Vacío = sin límite")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    responsable = models.CharField(max_length=20, choices=ResponsablePago.choices)

    class Meta:
        ordering = ["dia_desde"]

    def __str__(self):
        return f"Días {self.dia_desde}-{self.dia_hasta or '∞'}: {self.porcentaje}% {self.responsable}"


class Festivo(ModeloBase):
    """Festivos de Colombia para el cálculo de días hábiles (RN-005)."""

    fecha = models.DateField(unique=True)
    descripcion = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ["fecha"]
