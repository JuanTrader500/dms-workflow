from django.contrib import admin

from .models import Festivo, ParametroReconocimiento, ParametroSistema

admin.site.register(ParametroSistema)
admin.site.register(ParametroReconocimiento)
admin.site.register(Festivo)
