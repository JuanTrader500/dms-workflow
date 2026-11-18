"""Validación de consistencia de datos extraídos vs. registrados (RF-008).

Función pura (sin Django) para poder probarla sin base de datos.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from difflib import SequenceMatcher

UMBRAL_SIMILITUD_NOMBRE = 0.90


@dataclass(frozen=True)
class DatosRegistrados:
    nombre: str | None = None
    identificacion: str | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    dias: int | None = None
    entidad: str | None = None


@dataclass(frozen=True)
class DatosIA:
    nombre_colaborador: str | None = None
    numero_identificacion: str | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    dias_incapacidad: int | None = None
    entidad_emisora: str | None = None


@dataclass
class ResultadoConsistencia:
    coincide: bool
    discrepancias: list[dict] = field(default_factory=list)


def normalizar_texto(texto: str | None) -> str:
    if not texto:
        return ""
    sin_tildes = "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", sin_tildes).strip().lower()


def solo_digitos(texto: str | None) -> str:
    return re.sub(r"\D", "", texto or "")


def similitud(a: str | None, b: str | None) -> float:
    return SequenceMatcher(None, normalizar_texto(a), normalizar_texto(b)).ratio()


def comparar(registrado: DatosRegistrados, extraido: DatosIA) -> ResultadoConsistencia:
    """Compara campo a campo. Un campo no extraído (None) no se considera discrepancia: se marca como no verificable."""
    disc: list[dict] = []

    def agregar(campo, manual, ia, motivo):
        disc.append({"campo": campo, "registrado": str(manual), "extraido": str(ia), "motivo": motivo})

    if extraido.numero_identificacion is not None and registrado.identificacion is not None:
        if solo_digitos(extraido.numero_identificacion) != solo_digitos(registrado.identificacion):
            agregar("identificacion", registrado.identificacion, extraido.numero_identificacion, "no coincide")

    if extraido.nombre_colaborador and registrado.nombre:
        if similitud(extraido.nombre_colaborador, registrado.nombre) < UMBRAL_SIMILITUD_NOMBRE:
            agregar("nombre", registrado.nombre, extraido.nombre_colaborador, "similitud insuficiente")

    for campo, manual, ia in (
        ("fecha_inicio", registrado.fecha_inicio, extraido.fecha_inicio),
        ("fecha_fin", registrado.fecha_fin, extraido.fecha_fin),
        ("dias", registrado.dias, extraido.dias_incapacidad),
    ):
        if ia is not None and manual is not None and ia != manual:
            agregar(campo, manual, ia, "no coincide")

    # Coherencia interna: dias == fecha_fin - fecha_inicio + 1
    if extraido.fecha_inicio and extraido.fecha_fin and extraido.dias_incapacidad is not None:
        esperado = (extraido.fecha_fin - extraido.fecha_inicio).days + 1
        if esperado != extraido.dias_incapacidad:
            agregar("dias_coherencia", esperado, extraido.dias_incapacidad, "los días no coinciden con las fechas")

    if extraido.entidad_emisora and registrado.entidad:
        if similitud(extraido.entidad_emisora, registrado.entidad) < UMBRAL_SIMILITUD_NOMBRE:
            agregar("entidad", registrado.entidad, extraido.entidad_emisora, "entidad distinta")

    return ResultadoConsistencia(coincide=not disc, discrepancias=disc)


def decidir_estado(resultado: ResultadoConsistencia, confianza: float, umbral: float = 0.85) -> str:
    """RF-008 + decisión 10: confianza < umbral => verificación manual; discrepancias => en revisión."""
    if confianza < umbral:
        return "VERIFICACION_MANUAL"
    if not resultado.coincide:
        return "EN_REVISION"
    return "VALIDADO"
