"""CA-01..CA-08: flujo crítico completo. TODO(T-41): implementar cuando existan T-10..T-29."""

import pytest


@pytest.mark.skip(reason="Pendiente T-41")
def test_registro_extraccion_radicacion():
    """Registro -> checklist -> carga -> extracción (FakeExtractor) -> VALIDADA -> radicación -> TRANSCRITA -> alerta."""
