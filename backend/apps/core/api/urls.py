from django.urls import path

from . import views

urlpatterns = [
    path("config/parametros/", views.ParametrosView.as_view(), name="config-parametros"),
    path("config/reconocimiento/", views.ReconocimientoConfigView.as_view(), name="config-reconocimiento"),
    path("salud/", views.salud, name="salud"),
]
