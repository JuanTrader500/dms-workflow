"""Esquemas Pydantic de extracción (RF-007).

REGLA INQUEBRANTABLE: no existen campos de diagnóstico, código CIE, médico ni observaciones clínicas.
`extra="forbid"` + descarte explícito en el servicio garantizan que no se persista nada más.
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from apps.core.enums import TipoDocumento


class ExtraccionCertificadoIncapacidad(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nombre_colaborador: str | None = Field(None, description="Nombre completo del paciente/colaborador")
    numero_identificacion: str | None = Field(None, description="Número de documento de identidad, solo dígitos")
    fecha_inicio: date | None = Field(None, description="Fecha de inicio de la incapacidad (ISO 8601)")
    fecha_fin: date | None = Field(None, description="Fecha de finalización de la incapacidad (ISO 8601)")
    dias_incapacidad: int | None = Field(None, description="Número de días de incapacidad")
    entidad_emisora: str | None = Field(None, description="EPS/ARL o IPS que emite el certificado")
    confianza_global: float = Field(..., ge=0.0, le=1.0, description="Autoevaluación de legibilidad y completitud, 0 a 1")


# RF-006: el tipo etiquetado selecciona el esquema. Solo estos tipos se envían a la IA en el MVP.
ESQUEMAS_POR_TIPO: dict[str, type[BaseModel]] = {
    TipoDocumento.CERTIFICADO_INCAPACIDAD: ExtraccionCertificadoIncapacidad,
}

CAMPOS_OPERATIVOS = tuple(
    c for c in ExtraccionCertificadoIncapacidad.model_fields if c != "confianza_global"
)
