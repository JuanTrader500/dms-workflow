from django.contrib import admin

from .models import AuditoriaGestion

for modelo in (AuditoriaGestion,):
    admin.site.register(modelo)
