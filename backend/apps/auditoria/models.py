"""AuditoriaGestion INMUTABLE (RF-024, RNF-005): solo inserciones."""

from django.conf import settings
from django.db import models


class AuditoriaInmutableError(Exception):
    pass


class AuditoriaQuerySet(models.QuerySet):
    def update(self, **kwargs):
        raise AuditoriaInmutableError("Los registros de auditoría no se pueden modificar.")

    def delete(self):
        raise AuditoriaInmutableError("Los registros de auditoría no se pueden eliminar.")

    def bulk_update(self, objs, fields, batch_size=None):
        raise AuditoriaInmutableError("Los registros de auditoría no se pueden modificar.")


class AuditoriaGestion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                help_text="Vacío = Sistema (jobs automáticos)")
    incapacidad = models.ForeignKey("incapacidades.Incapacidad", null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name="auditoria")
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)  # ISO 8601 al serializar
    accion = models.CharField(max_length=60)
    detalle = models.JSONField(default=dict, blank=True)

    objects = AuditoriaQuerySet.as_manager()

    class Meta:
        ordering = ["-timestamp"]

    def save(self, *args, **kwargs):
        if not self._state.adding:
            raise AuditoriaInmutableError("Los registros de auditoría no se pueden modificar.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise AuditoriaInmutableError("Los registros de auditoría no se pueden eliminar.")
