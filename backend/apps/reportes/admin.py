from django.contrib import admin

from .models import ReporteAusentismo

for modelo in (ReporteAusentismo,):
    admin.site.register(modelo)
