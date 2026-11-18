"""Clientes de extracción (RF-007, RNF-007).

- `ExtractorIA`: interfaz común.
- `GeminiExtractor`: llamada real a Gemini con salida estructurada, timeout y reintentos.
- `FakeExtractor`: determinista, para pruebas y demo sin API key.

Nunca se registran en logs el contenido del documento ni la respuesta cruda.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Protocol

from apps.core.exceptions import IAIndisponible, IARespuestaInvalida

from .prompts import PROMPT_SISTEMA

log = logging.getLogger(__name__)


@dataclass
class ResultadoExtraccion:
    datos: dict                      # solo campos operativos declarados en el esquema
    confianza: float
    campos_descartados: int = 0      # cantidad de claves no declaradas que se ignoraron (sin guardar su valor)


class ExtractorIA(Protocol):
    def extraer(self, contenido: bytes, mime_type: str, tipo_documento: str) -> ResultadoExtraccion: ...


class GeminiExtractor:
    def __init__(self, api_key: str, modelo: str, timeout_s: int = 10, reintentos: int = 2):
        if not api_key:
            raise IAIndisponible("GEMINI_API_KEY no configurada.")
        self.api_key, self.modelo, self.timeout_s, self.reintentos = api_key, modelo, timeout_s, reintentos

    def extraer(self, contenido: bytes, mime_type: str, tipo_documento: str) -> ResultadoExtraccion:
        from .schemas import CAMPOS_OPERATIVOS, ESQUEMAS_POR_TIPO

        esquema = ESQUEMAS_POR_TIPO.get(tipo_documento)
        if esquema is None:
            raise IARespuestaInvalida("Tipo de documento sin esquema de extracción.")

        try:  # importación diferida: las pruebas unitarias no requieren el SDK
            from google import genai
            from google.genai import types
        except ImportError as exc:  # pragma: no cover
            raise IAIndisponible("SDK google-genai no instalado.") from exc

        cliente = genai.Client(api_key=self.api_key)
        config = types.GenerateContentConfig(
            system_instruction=PROMPT_SISTEMA,
            response_mime_type="application/json",
            response_schema=esquema,
            temperature=0,
            http_options=types.HttpOptions(timeout=self.timeout_s * 1000),
        )
        ultimo_error: Exception | None = None
        for intento in range(self.reintentos + 1):
            try:
                respuesta = cliente.models.generate_content(
                    model=self.modelo,
                    contents=[types.Part.from_bytes(data=contenido, mime_type=mime_type), "Extrae los datos operativos."],
                    config=config,
                )
                bruto = respuesta.parsed
                if bruto is None:
                    raise IARespuestaInvalida()
                datos = bruto.model_dump() if hasattr(bruto, "model_dump") else dict(bruto)
                confianza = float(datos.pop("confianza_global", 0.0))
                operativos = {k: datos.get(k) for k in CAMPOS_OPERATIVOS}
                descartados = len([k for k in datos if k not in CAMPOS_OPERATIVOS])
                return ResultadoExtraccion(datos=operativos, confianza=confianza, campos_descartados=descartados)
            except IARespuestaInvalida:
                raise
            except Exception as exc:  # timeout, 429, 5xx, red
                ultimo_error = exc
                log.warning("Fallo Gemini (intento %s/%s): %s", intento + 1, self.reintentos + 1, type(exc).__name__)
                if intento < self.reintentos:
                    time.sleep((1, 3)[min(intento, 1)])  # backoff 1 s, 3 s
        raise IAIndisponible() from ultimo_error


@dataclass
class FakeExtractor:
    """Devuelve datos fijos. Permite simular escenarios (confianza baja, discrepancia, caída)."""

    datos: dict = field(default_factory=dict)
    confianza: float = 0.95
    falla: bool = False

    def extraer(self, contenido: bytes, mime_type: str, tipo_documento: str) -> ResultadoExtraccion:
        if self.falla:
            raise IAIndisponible()
        return ResultadoExtraccion(datos=dict(self.datos), confianza=self.confianza)


def obtener_extractor() -> ExtractorIA:
    from django.conf import settings

    if settings.IA_PROVEEDOR == "fake":
        return FakeExtractor()
    return GeminiExtractor(settings.GEMINI_API_KEY, settings.GEMINI_MODEL, settings.GEMINI_TIMEOUT_SECONDS)
