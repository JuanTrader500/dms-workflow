"""RF-017 / RN-013 / CA-07: límites de los tramos."""

from decimal import Decimal

import pytest

from apps.cobro.services.reconocimiento import calcular_desglose, responsable_en_dia


@pytest.mark.parametrize(
    "dia,esperado",
    [(1, "SERTESA"), (2, "SERTESA"), (3, "EPS"), (90, "EPS"), (91, "EPS"), (180, "EPS"), (181, "COLABORADOR")],
)
def test_responsable_por_dia(dia, esperado):
    assert responsable_en_dia(dia) == esperado


def test_desglose_incapacidad_de_100_dias():
    lineas = calcular_desglose(100)
    assert [(l.dia_desde, l.dia_hasta, l.dias, l.porcentaje) for l in lineas] == [
        (1, 2, 2, Decimal("100")),
        (3, 90, 88, Decimal("67")),
        (91, 100, 10, Decimal("50")),
    ]


def test_desglose_mas_de_180_dias_incluye_tramo_colaborador():
    lineas = calcular_desglose(200)
    assert lineas[-1].responsable == "COLABORADOR"
    assert lineas[-1].dias == 20


def test_valor_con_ibc():
    lineas = calcular_desglose(2, ibc=Decimal("3000000"))
    assert lineas[0].valor == Decimal("200000.00")  # 2 días * (3.000.000/30) * 100 %
