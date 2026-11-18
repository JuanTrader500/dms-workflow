from django.contrib import admin

from . import models

for modelo in (
    models.Incapacidad,
    models.ReglaDocumental,
    models.ChecklistDocumental,
    models.ItemChecklist,
    models.AvisoSubsanacion,
    models.AlertaPlazo,
    models.ConceptoRehabilitacion,
):
    admin.site.register(modelo)
