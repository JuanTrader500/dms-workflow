import pytest
from rest_framework.test import APIClient

from apps.core.enums import RolUsuario


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def auxiliar(db, django_user_model):
    return django_user_model.objects.create_user(username="aux", password="x", rol=RolUsuario.AUXILIAR_ADMIN_PERSONAL)


@pytest.fixture
def colaborador_rol(db, django_user_model):
    return django_user_model.objects.create_user(username="col", password="x", rol=RolUsuario.COLABORADOR)
