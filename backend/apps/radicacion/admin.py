from django.contrib import admin

from .models import Radicacion

for modelo in (Radicacion,):
    admin.site.register(modelo)
