from django.contrib import admin

from .models import Notificacion

for modelo in (Notificacion,):
    admin.site.register(modelo)
