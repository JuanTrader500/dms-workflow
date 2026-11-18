"""Enumeraciones del dominio. Nombres idénticos a los del diagrama de clases."""

from django.db import models


class RolUsuario(models.TextChoices):
    COLABORADOR = "COLABORADOR", "Colaborador"
    AUXILIAR_ADMIN_PERSONAL = "AUXILIAR_ADMIN_PERSONAL", "Auxiliar de Administración de Personal"
    LIDER = "LIDER", "Líder"
    CARTERA = "CARTERA", "Área de Cartera"
    JURIDICA = "JURIDICA", "Área Jurídica"
    CONTABILIDAD = "CONTABILIDAD", "Contabilidad / Tesorería"
    GESTION_DOCUMENTAL = "GESTION_DOCUMENTAL", "Gestión Documental"


class EstadoCaso(models.TextChoices):
    REGISTRADA = "REGISTRADA", "Registrada"
    DOC_INCOMPLETA = "DOC_INCOMPLETA", "Documentación incompleta"
    PENDIENTE_DECISION_ADMIN = "PENDIENTE_DECISION_ADMIN", "Pendiente de decisión administrativa"
    EN_REVISION_INCONSISTENCIA = "EN_REVISION_INCONSISTENCIA", "En revisión por inconsistencia"
    VALIDADA = "VALIDADA", "Validada"
    TRANSCRITA = "TRANSCRITA", "Transcrita"
    COBRADA = "COBRADA", "Cobrada"
    PAGADA = "PAGADA", "Pagada"
    RECHAZADA = "RECHAZADA", "Rechazada"
    ARCHIVADA = "ARCHIVADA", "Archivada"


class TipoCaso(models.TextChoices):
    ENFERMEDAD_GENERAL = "ENFERMEDAD_GENERAL", "Enfermedad general"
    ACCIDENTE_LABORAL = "ACCIDENTE_LABORAL", "Accidente laboral"
    ACCIDENTE_TRANSITO = "ACCIDENTE_TRANSITO", "Accidente de tránsito"
    LICENCIA_MATERNIDAD = "LICENCIA_MATERNIDAD", "Licencia de maternidad"
    LICENCIA_PATERNIDAD = "LICENCIA_PATERNIDAD", "Licencia de paternidad"


class CanalRecepcion(models.TextChoices):
    RECEPCION_FISICA = "RECEPCION_FISICA", "Recepción física"
    OFICINAS_PRINCIPALES = "OFICINAS_PRINCIPALES", "Oficinas principales"
    LIDERES_COMERCIALES = "LIDERES_COMERCIALES", "Líderes comerciales"
    CORREO_ELECTRONICO = "CORREO_ELECTRONICO", "Correo electrónico"


class TipoDocumento(models.TextChoices):
    CERTIFICADO_INCAPACIDAD = "CERTIFICADO_INCAPACIDAD", "Certificado de incapacidad"
    EPICRISIS = "EPICRISIS", "Epicrisis"
    HISTORIA_CLINICA = "HISTORIA_CLINICA", "Historia clínica"
    FURIPS = "FURIPS", "FURIPS"
    REGISTRO_CIVIL = "REGISTRO_CIVIL", "Registro civil"
    OTRO = "OTRO", "Otro"


# Documentos de salud reservada: se almacenan pero NUNCA se envían a la IA y se destruyen al archivar (RN-016).
DOCUMENTOS_CLINICOS = frozenset({TipoDocumento.EPICRISIS, TipoDocumento.HISTORIA_CLINICA})
# Tipos con esquema de extracción en el MVP (RF-007).
DOCUMENTOS_EXTRAIBLES_IA = frozenset({TipoDocumento.CERTIFICADO_INCAPACIDAD})


class EstadoItem(models.TextChoices):
    PENDIENTE = "PENDIENTE", "Pendiente"
    CARGADO = "CARGADO", "Cargado"


class EstadoValidacion(models.TextChoices):
    PENDIENTE = "PENDIENTE", "Pendiente"
    VALIDADO = "VALIDADO", "Validado"
    EN_REVISION = "EN_REVISION", "En revisión por inconsistencia"
    VERIFICACION_MANUAL = "VERIFICACION_MANUAL", "Verificación manual"
    CONFIRMADO_MANUAL = "CONFIRMADO_MANUAL", "Confirmado manualmente"


class TipoEntidad(models.TextChoices):
    EPS = "EPS", "EPS"
    ARL = "ARL", "ARL"


class TipoAlerta(models.TextChoices):
    REMISION_TARDIA = "REMISION_TARDIA", "Remisión tardía"
    SUBSANACION = "SUBSANACION", "Subsanación documental"
    VENCIMIENTO_TRANSCRIPCION = "VENCIMIENTO_TRANSCRIPCION", "Vencimiento de transcripción"
    UMBRAL_DIAS = "UMBRAL_DIAS", "Umbral de días de incapacidad"
    REHABILITACION = "REHABILITACION", "Concepto de rehabilitación"


class ResultadoConcepto(models.TextChoices):
    FAVORABLE = "FAVORABLE", "Favorable"
    DESFAVORABLE = "DESFAVORABLE", "Desfavorable"


class EstadoCobro(models.TextChoices):
    PENDIENTE = "PENDIENTE", "Pendiente"
    EN_GESTION = "EN_GESTION", "En gestión"
    PAGADO = "PAGADO", "Pagado"


class DecisionFinal(models.TextChoices):
    RECUPERAR = "RECUPERAR", "Recuperar"
    DAR_DE_BAJA = "DAR_DE_BAJA", "Dar de baja"


class ResponsablePago(models.TextChoices):
    SERTESA = "SERTESA", "Sertesa"
    EPS = "EPS", "EPS"
    COLABORADOR = "COLABORADOR", "Colaborador"
