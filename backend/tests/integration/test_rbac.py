"""RF-025 / CA-09: un colaborador no puede acceder a recursos de gestión."""

import pytest


@pytest.mark.django_db
def test_colaborador_no_puede_ver_datos_extraidos(api, colaborador_rol):
    api.force_authenticate(colaborador_rol)
    assert api.get("/api/v1/datos-extraidos/").status_code == 403


@pytest.mark.django_db
def test_auxiliar_si_puede(api, auxiliar):
    api.force_authenticate(auxiliar)
    assert api.get("/api/v1/datos-extraidos/").status_code == 200
