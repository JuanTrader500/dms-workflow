from django.contrib import admin

from .models import ConciliacionContable

for modelo in (ConciliacionContable,):
    admin.site.register(modelo)
