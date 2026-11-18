"""Núcleo del dominio: Incapacidad, checklist, avisos, alertas y concepto de rehabilitación."""

from django.conf import settings
from django.db import models
from django.db.models import F, Q

from apps.core.enums import (
    CanalRecepcion,
    EstadoCaso,
    EstadoItem,
    ResultadoConcepto,
    TipoAlerta,
    TipoCaso,
    TipoDocumento,
)
from apps.core.models import ModeloBase


class Incapacidad(ModeloBase):
    colaborador = models.ForeignKey("usuarios.Colaborador", on_delete=models.PROTECT, related_name="incapacidades")
    entidad = models.ForeignKey(
        "entidades.EntidadEPSARL", null=True, blank=True, on_delete=models.PROTECT, related_name="incapacidades"
    )
    responsable_actual = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="casos_a_cargo"
    )
    tipo_caso = models.CharField(max_length=30, choices=TipoCaso.choices)
    canal = models.CharField(max_length=30, choices=CanalRecepcion.choices)
    estado = models.CharField(max_length=30, choices=EstadoCaso.choices, default=EstadoCaso.REGISTRADA, db_index=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    dias_incapacidad = models.PositiveIntegerField(null=True, blank=True)
    fecha_expedicion = models.DateField(null=True, blank=True)
    fecha_remision = models.DateField(null=True, blank=True)
    remision_tardia = models.BooleanField(default=False)
    fecha_limite_transcripcion = models.DateField(null=True, blank=True)
    fecha_inicio_cobro = models.DateField(null=True, blank=True, help_text="Primer requerimiento persuasivo (RN-015)")

    class Meta:
        ordering = ["-creado_en"]
        verbose_name_plural = "incapacidades"
        constraints = [
            models.CheckConstraint(
                condition=Q(fecha_fin__isnull=True) | Q(fecha_fin__gte=F("fecha_inicio")),
                name="ck_incapacidad_fechas",
            )
        ]

    def calcular_dias_transcurridos(self, hoy) -> int:
        return (hoy - self.fecha_inicio).days + 1

    def __str__(self):
        return f"Caso {self.pk} - {self.colaborador.nombre} ({self.estado})"


class ReglaDocumental(ModeloBase):
    """Tabla de documentos requeridos por tipo de caso (RN-004). Editable."""

    tipo_caso = models.CharField(max_length=30, choices=TipoCaso.choices)
    tipo_documento = models.CharField(max_length=30, choices=TipoDocumento.choices)
    obligatorio = models.BooleanField(default=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["tipo_caso", "tipo_documento"], name="uq_regla_documental")]


class ChecklistDocumental(ModeloBase):
    incapacidad = models.OneToOneField(Incapacidad, on_delete=models.CASCADE, related_name="checklist")
    completo = models.BooleanField(default=False)


class ItemChecklist(ModeloBase):
    checklist = models.ForeignKey(ChecklistDocumental, on_delete=models.CASCADE, related_name="items")
    tipo_requerido = models.CharField(max_length=30, choices=TipoDocumento.choices)
    estado = models.CharField(max_length=10, choices=EstadoItem.choices, default=EstadoItem.PENDIENTE)
    documento = models.ForeignKey(
        "documentos.DocumentoSoporte", null=True, blank=True, on_delete=models.SET_NULL, related_name="items"
    )


class AvisoSubsanacion(ModeloBase):
    """Máximo dos avisos por caso (RN-005, diagrama: 0..2)."""

    incapacidad = models.ForeignKey(Incapacidad, on_delete=models.CASCADE, related_name="avisos")
    numero = models.PositiveSmallIntegerField()
    fecha_envio = models.DateField()
    fecha_limite = models.DateField()
    respondido = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["incapacidad", "numero"], name="uq_aviso_numero"),
            models.CheckConstraint(condition=Q(numero__in=[1, 2]), name="ck_aviso_numero"),
        ]


class AlertaPlazo(ModeloBase):
    incapacidad = models.ForeignKey(Incapacidad, on_delete=models.CASCADE, related_name="alertas")
    tipo = models.CharField(max_length=30, choices=TipoAlerta.choices)
    umbral_dias = models.PositiveIntegerField(null=True, blank=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    atendida = models.BooleanField(default=False)
    mensaje = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-fecha_generacion"]
        constraints = [
            # Idempotencia de los jobs: una alerta por (caso, tipo, umbral)
            models.UniqueConstraint(fields=["incapacidad", "tipo", "umbral_dias"], name="uq_alerta_caso_tipo_umbral"),
        ]


class ConceptoRehabilitacion(ModeloBase):
    incapacidad = models.OneToOneField(Incapacidad, on_delete=models.CASCADE, related_name="concepto_rehabilitacion")
    fecha_emision = models.DateField()
    resultado = models.CharField(max_length=15, choices=ResultadoConcepto.choices)
    fecha_remision_afp = models.DateField(null=True, blank=True)
