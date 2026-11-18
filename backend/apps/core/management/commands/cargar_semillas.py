"""Carga idempotente de datos de configuración y datos demo.

Solo se siembran datos presentes en el documento fuente (SRS). Todo lo demás debe
completarse desde la configuración editable (RNF-008) — no inventar valores.
"""

from decimal import Decimal

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.core.enums import ResponsablePago, RolUsuario, TipoCaso, TipoDocumento, TipoEntidad
from apps.core.models import ParametroReconocimiento, ParametroSistema


class Command(BaseCommand):
    help = "Carga semillas de configuración (y usuarios demo si SEED_DEMO=1)."

    def handle(self, *args, **opciones):
        self._parametros()
        self._reconocimiento()
        self._entidades_y_plazos()
        self._reglas_documentales()
        if settings.SEED_DEMO:
            self._demo()
        self.stdout.write(self.style.SUCCESS("Semillas cargadas."))

    def _parametros(self):
        valores = [
            ("IA_UMBRAL_CONFIANZA", "0.85", "Confianza mínima para aceptar una extracción (decisión 10)"),
            ("DIAS_PLAZO_SUBSANACION", "3", "Días hábiles para subsanar documentación (RN-005)"),
            ("DIAS_REMISION_MAX", "2", "Días máximos de remisión del colaborador (RN-003)"),
            ("DIAS_ESCALAMIENTO_CARTERA", "180", "Días sin pago para escalar a Cartera (RN-015)"),
            ("UMBRALES_DIAS", "90,120,150,180", "Umbrales de alerta de incapacidad prolongada (RN-014)"),
            ("DIAS_ALERTA_PREVIA_TRANSCRIPCION", "5", "Antelación de la alerta de vencimiento (valor inicial propuesto, parametrizable)"),
            ("DIAS_REPORTE_AUSENTISMO", "3", "Primeros días del mes para remitir el reporte (RN-017)"),
        ]
        for clave, valor, desc in valores:
            ParametroSistema.objects.get_or_create(clave=clave, defaults={"valor": valor, "descripcion": desc})

    def _reconocimiento(self):
        tramos = [
            (1, 2, "100", ResponsablePago.SERTESA),
            (3, 90, "67", ResponsablePago.EPS),
            (91, 180, "50", ResponsablePago.EPS),
            (181, None, "0", ResponsablePago.COLABORADOR),
        ]
        for desde, hasta, pct, resp in tramos:
            ParametroReconocimiento.objects.get_or_create(
                dia_desde=desde, defaults={"dia_hasta": hasta, "porcentaje": Decimal(pct), "responsable": resp}
            )

    def _entidades_y_plazos(self):
        from apps.entidades.models import EntidadEPSARL, PlazoTranscripcion

        # RN-006: SOS, Sanitas y Famisanar transcriben solo por correo. Salud Total aparece en RN-007 (tránsito).
        entidades = {"SOS": True, "Sanitas": True, "Famisanar": True, "Salud Total": False}
        objetos = {}
        for nombre, por_correo in entidades.items():
            objetos[nombre], _ = EntidadEPSARL.objects.get_or_create(
                nombre=nombre, defaults={"tipo": TipoEntidad.EPS, "transcripcion_por_correo": por_correo}
            )
        # Plazos conocidos del documento fuente
        PlazoTranscripcion.objects.get_or_create(
            entidad=objetos["Salud Total"], tipo_caso=TipoCaso.ACCIDENTE_TRANSITO, defaults={"plazo_dias": 15}
        )
        PlazoTranscripcion.objects.get_or_create(
            entidad=objetos["Sanitas"], tipo_caso=None, defaults={"plazo_dias": 3 * 365}
        )
        for ent in objetos.values():  # licencias de paternidad: 30 días calendario en todas las EPS
            PlazoTranscripcion.objects.get_or_create(
                entidad=ent, tipo_caso=TipoCaso.LICENCIA_PATERNIDAD, defaults={"plazo_dias": 30}
            )

    def _reglas_documentales(self):
        """Semilla PROVISIONAL (editable): el SRS no lista el detalle por tipo, solo el FURIPS de tránsito."""
        from apps.incapacidades.models import ReglaDocumental

        for tipo in TipoCaso.values:
            ReglaDocumental.objects.get_or_create(
                tipo_caso=tipo, tipo_documento=TipoDocumento.CERTIFICADO_INCAPACIDAD, defaults={"obligatorio": True}
            )
        ReglaDocumental.objects.get_or_create(
            tipo_caso=TipoCaso.ACCIDENTE_TRANSITO, tipo_documento=TipoDocumento.FURIPS, defaults={"obligatorio": True}
        )
        for tipo in (TipoCaso.LICENCIA_MATERNIDAD, TipoCaso.LICENCIA_PATERNIDAD):
            ReglaDocumental.objects.get_or_create(
                tipo_caso=tipo, tipo_documento=TipoDocumento.REGISTRO_CIVIL, defaults={"obligatorio": True}
            )

    def _demo(self):
        from apps.usuarios.models import Colaborador, Usuario

        if not settings.DEMO_PASSWORD:
            self.stdout.write(self.style.WARNING("SEED_DEMO activo pero DEMO_PASSWORD vacío: se omiten usuarios demo."))
            return
        for rol in RolUsuario.values:
            nombre = rol.lower()
            usuario, creado = Usuario.objects.get_or_create(
                username=nombre, defaults={"rol": rol, "email": f"{nombre}@demo.local"}
            )
            if creado:
                usuario.set_password(settings.DEMO_PASSWORD)
                usuario.save()
        ficticios = [("1000000001", "Colaborador Ficticio Uno"), ("1000000002", "Colaborador Ficticio Dos")]
        for ident, nombre in ficticios:
            Colaborador.objects.get_or_create(
                identificacion=ident,
                defaults={"nombre": nombre, "cargo": "Operario", "email": f"{ident}@demo.local", "activo": True},
            )
