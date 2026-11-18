"""Planificador diario (APScheduler, zona America/Bogota). Se lanza desde entrypoint.sh."""

import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand

from apps.scheduler import jobs

log = logging.getLogger(__name__)
ZONA = "America/Bogota"


class Command(BaseCommand):
    help = "Ejecuta los jobs programados de alertas y reportes."

    def handle(self, *args, **opciones):
        s = BlockingScheduler(timezone=ZONA)
        s.add_job(jobs.alertas_transcripcion, CronTrigger(hour=7, minute=0, timezone=ZONA), id="alertas_transcripcion")
        s.add_job(jobs.alertas_umbral_dias, CronTrigger(hour=7, minute=10, timezone=ZONA), id="alertas_umbral_dias")
        s.add_job(jobs.plazo_subsanacion, CronTrigger(hour=7, minute=20, timezone=ZONA), id="plazo_subsanacion")
        s.add_job(jobs.escalamiento_cartera, CronTrigger(hour=7, minute=30, timezone=ZONA), id="escalamiento_cartera")
        s.add_job(jobs.reporte_ausentismo, CronTrigger(day=1, hour=6, minute=0, timezone=ZONA), id="reporte_ausentismo")
        log.info("Planificador iniciado con %d jobs", len(s.get_jobs()))
        try:
            s.start()
        except (KeyboardInterrupt, SystemExit):
            log.info("Planificador detenido")
