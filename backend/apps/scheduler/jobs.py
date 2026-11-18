"""Jobs programados. TODOS deben ser idempotentes y auditar como "Sistema" (RF-013, RF-014, RNF-002)."""

from __future__ import annotations

import logging
from datetime import date

from django.utils import timezone

log = logging.getLogger(__name__)


def _hoy() -> date:
    return timezone.localdate()


def alertas_transcripcion() -> None:
    """RF-013. TODO(T-31): incapacidades.services.alertas.generar_alertas_transcripcion(_hoy())."""
    log.info("[job] alertas_transcripcion (pendiente T-31)")


def alertas_umbral_dias() -> None:
    """RF-014/RF-015. TODO(T-36)."""
    log.info("[job] alertas_umbral_dias (pendiente T-36)")


def plazo_subsanacion() -> None:
    """RF-005. TODO(T-34)."""
    log.info("[job] plazo_subsanacion (pendiente T-34)")


def reporte_ausentismo() -> None:
    """RF-021. TODO(T-38): día 1 de cada mes genera el reporte del mes anterior."""
    log.info("[job] reporte_ausentismo (pendiente T-38)")


def escalamiento_cartera() -> None:
    """RF-019 (post-MVP). TODO(T-46)."""
    log.info("[job] escalamiento_cartera (pendiente T-46)")
