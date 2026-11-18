"""Reconocimiento económico por tramos (RF-017, RN-013).

Núcleo PURO (sin Django): los tramos se inyectan, por defecto los de RN-013.
`obtener_tramos_configurados()` los lee de core.ParametroReconocimiento (editable, RNF-008).

SUPUESTO A CONFIRMAR: el valor diario del IBC se calcula como IBC/30. El SRS no define la fórmula monetaria;
si no hay IBC, el desglose solo informa días, porcentaje y responsable.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

DIVISOR_IBC_DIARIO = Decimal(30)


@dataclass(frozen=True)
class Tramo:
    dia_desde: int
    dia_hasta: int | None
    porcentaje: Decimal
    responsable: str


TRAMOS_RN013 = (
    Tramo(1, 2, Decimal("100"), "SERTESA"),
    Tramo(3, 90, Decimal("67"), "EPS"),
    Tramo(91, 180, Decimal("50"), "EPS"),
    Tramo(181, None, Decimal("0"), "COLABORADOR"),  # trámite a cargo del colaborador (AFP/EPS)
)


@dataclass(frozen=True)
class LineaDesglose:
    dia_desde: int
    dia_hasta: int
    dias: int
    porcentaje: Decimal
    responsable: str
    valor: Decimal | None


def calcular_desglose(dias_incapacidad: int, ibc: Decimal | None = None, tramos=TRAMOS_RN013) -> list[LineaDesglose]:
    """Divide los días de la incapacidad en tramos y asigna porcentaje/responsable a cada uno."""
    if dias_incapacidad < 1:
        return []
    lineas: list[LineaDesglose] = []
    for t in sorted(tramos, key=lambda x: x.dia_desde):
        if dias_incapacidad < t.dia_desde:
            break
        hasta = dias_incapacidad if t.dia_hasta is None else min(dias_incapacidad, t.dia_hasta)
        dias = hasta - t.dia_desde + 1
        valor = None
        if ibc is not None:
            valor = (ibc / DIVISOR_IBC_DIARIO * dias * t.porcentaje / Decimal(100)).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        lineas.append(LineaDesglose(t.dia_desde, hasta, dias, t.porcentaje, t.responsable, valor))
    return lineas


def responsable_en_dia(dia: int, tramos=TRAMOS_RN013) -> str:
    for t in tramos:
        if dia >= t.dia_desde and (t.dia_hasta is None or dia <= t.dia_hasta):
            return t.responsable
    raise ValueError(f"Día fuera de rango: {dia}")


def obtener_tramos_configurados() -> tuple[Tramo, ...]:
    """Lee los tramos editables de la BD (RNF-008); si no hay, usa los de RN-013."""
    from apps.core.models import ParametroReconocimiento

    filas = list(ParametroReconocimiento.objects.all())
    if not filas:
        return TRAMOS_RN013
    return tuple(Tramo(f.dia_desde, f.dia_hasta, f.porcentaje, f.responsable) for f in filas)
