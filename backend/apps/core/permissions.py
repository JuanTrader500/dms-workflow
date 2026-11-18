"""RBAC (RF-025). Cada vista declara roles_lectura y roles_escritura; sin declaración => denegado."""

from rest_framework.permissions import SAFE_METHODS, BasePermission


class TienePermisoRol(BasePermission):
    message = "Su rol no tiene permiso para esta acción."

    def has_permission(self, request, view):
        usuario = request.user
        if not usuario or not usuario.is_authenticated:
            return False
        if usuario.is_superuser:
            return True
        atributo = "roles_lectura" if request.method in SAFE_METHODS else "roles_escritura"
        roles = getattr(view, atributo, None)
        return bool(roles) and usuario.rol in roles
