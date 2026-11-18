from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Colaborador, Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Rol DMS", {"fields": ("rol",)}),)
    list_display = ("username", "email", "rol", "is_active")


admin.site.register(Colaborador)
