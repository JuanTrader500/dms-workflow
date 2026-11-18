from django.contrib import admin

from .models import SeguimientoCobro, ReconocimientoEconomico, RequerimientoCobro, EscalamientoCartera, GestionJuridica

for modelo in (SeguimientoCobro, ReconocimientoEconomico, RequerimientoCobro, EscalamientoCartera, GestionJuridica,):
    admin.site.register(modelo)
