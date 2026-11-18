"""RF-008 / CA-04: validación de consistencia IA vs. registro."""

from datetime import date

from apps.ia.services.consistencia import DatosIA, DatosRegistrados, comparar, decidir_estado

REG = DatosRegistrados(
    nombre="Juan Pérez Gómez", identificacion="1000000001",
    fecha_inicio=date(2026, 11, 2), fecha_fin=date(2026, 11, 4), dias=3, entidad="Sanitas",
)


def ia(**cambios):
    base = dict(
        nombre_colaborador="JUAN PEREZ GOMEZ", numero_identificacion="1.000.000.001",
        fecha_inicio=date(2026, 11, 2), fecha_fin=date(2026, 11, 4), dias_incapacidad=3, entidad_emisora="SANITAS",
    )
    base.update(cambios)
    return DatosIA(**base)


def test_coincidencia_total_con_normalizacion():
    r = comparar(REG, ia())
    assert r.coincide and decidir_estado(r, 0.95) == "VALIDADO"


def test_dias_3_vs_30_bloquea():
    r = comparar(REG, ia(dias_incapacidad=30))
    assert not r.coincide
    assert decidir_estado(r, 0.95) == "EN_REVISION"


def test_confianza_baja_va_a_verificacion_manual():
    r = comparar(REG, ia())
    assert decidir_estado(r, 0.70) == "VERIFICACION_MANUAL"


def test_dias_incoherentes_con_fechas():
    r = comparar(REG, ia(fecha_fin=date(2026, 11, 10)))
    campos = {d["campo"] for d in r.discrepancias}
    assert "fecha_fin" in campos and "dias_coherencia" in campos
