"""Usuario del sistema (con rol, RF-025) y Colaborador (empleado que reporta incapacidades)."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.enums import RolUsuario
from apps.core.models import ModeloBase


class Usuario(AbstractUser):
    rol = models.CharField(max_length=30, choices=RolUsuario.choices, default=RolUsuario.COLABORADOR)

    def tiene_permiso(self, roles_permitidos) -> bool:
        return self.is_superuser or self.rol in roles_permitidos


class Colaborador(ModeloBase):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(
        "usuarios.Usuario", null=True, blank=True, on_delete=models.SET_NULL, related_name="colaborador"
    )

    def existe_y_activo(self) -> bool:
        return self.activo

    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"
