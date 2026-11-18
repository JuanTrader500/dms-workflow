"""Seguimiento de cobro, reconocimiento económico, cobro persuasivo, Cartera y Jurídica (RF-016..RF-020)."""

from django.db import models

from apps.core.enums import DecisionFinal, EstadoCobro, ResponsablePago
from apps.core.models import ModeloBase


class SeguimientoCobro(ModeloBase):
    incapacidad = models.ForeignKey("incapacidades.Incapacidad", on_delete=models.CASCADE, related_name="seguimientos_cobro")
    fecha = models.DateField()
    estado = models.CharField(max_length=15, choices=EstadoCobro.choices, default=EstadoCobro.PENDIENTE)
    saldo_adeudado = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    evidencia = models.FileField(upload_to="seguimientos/", null=True, blank=True)
    registrado_por = models.ForeignKey("usuarios.Usuario", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-fecha"]


class ReconocimientoEconomico(ModeloBase):
    incapacidad = models.OneToOneField("incapacidades.Incapacidad", on_delete=models.CASCADE, related_name="reconocimiento")
    ibc = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    responsable_pago = models.CharField(max_length=15, choices=ResponsablePago.choices, blank=True)
    desglose = models.JSONField(default=list, blank=True)


class RequerimientoCobro(ModeloBase):
    incapacidad = models.ForeignKey("incapacidades.Incapacidad", on_delete=models.CASCADE, related_name="requerimientos")
    numero = models.PositiveSmallIntegerField()
    fecha = models.DateField()
    fundamento_hecho = models.TextField()
    fundamento_derecho = models.TextField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["incapacidad", "numero"], name="uq_requerimiento_numero")]


class EscalamientoCartera(ModeloBase):
    incapacidad = models.OneToOneField("incapacidades.Incapacidad", on_delete=models.CASCADE, related_name="escalamiento_cartera")
    fecha_traslado = models.DateField()
    deterioro_crediticio = models.BooleanField(default=False)
    gestion_agotada = models.BooleanField(default=False)
    pago_recuperado = models.BooleanField(default=False)


class GestionJuridica(ModeloBase):
    escalamiento = models.OneToOneField(EscalamientoCartera, on_delete=models.CASCADE, related_name="gestion_juridica")
    fecha_traslado = models.DateField()
    decision_final = models.CharField(max_length=15, choices=DecisionFinal.choices, blank=True)
