"""RN-005: 3 días hábiles."""

from datetime import date

from apps.core.utils.dias_habiles import sumar_dias_habiles


def test_tres_dias_habiles_desde_lunes():
    assert sumar_dias_habiles(date(2026, 11, 16), 3) == date(2026, 11, 19)


def test_salta_fin_de_semana():
    assert sumar_dias_habiles(date(2026, 11, 19), 3) == date(2026, 11, 24)  # jue -> mar


def test_salta_festivo():
    assert sumar_dias_habiles(date(2026, 11, 16), 1, {date(2026, 11, 17)}) == date(2026, 11, 18)
