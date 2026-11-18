"""Orquestación de la extracción con IA (RF-006, RF-007, RF-008, RNF-007)."""

from __future__ import annotations



def extraer_datos(documento, usuario=None) -> 'DatosExtraidos':
    """Flujo: (1) si el tipo es clínico o sin esquema => VERIFICACION_MANUAL sin llamar a la IA; (2) preparar_para_ia; (3) obtener_extractor().extraer(); (4) IAIndisponible/IARespuestaInvalida => VERIFICACION_MANUAL en < 2 s sin perder datos (RNF-007); (5) descartar campos no declarados; (6) guardar DatosExtraidos SIN respuesta cruda; (7) comparar() + decidir_estado(); (8) si EN_REVISION => Incapacidad a EN_REVISION_INCONSISTENCIA vía estados.cambiar_estado; (9) auditar."""
    raise NotImplementedError("T-18")


def evaluar_caso(incapacidad, usuario=None) -> str:
    """Si el checklist está completo y todos los DatosExtraidos están VALIDADO => caso VALIDADA (RF-008)."""
    raise NotImplementedError("T-20")
