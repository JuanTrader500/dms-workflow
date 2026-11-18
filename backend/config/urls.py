"""Enrutamiento raíz. Todas las rutas de negocio viven bajo /api/v1/."""

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_v1 = [
    path("auth/", include("apps.usuarios.api.auth_urls")),
    path("", include("apps.usuarios.api.urls")),
    path("", include("apps.entidades.api.urls")),
    path("", include("apps.incapacidades.api.urls")),
    path("", include("apps.documentos.api.urls")),
    path("", include("apps.ia.api.urls")),
    path("", include("apps.radicacion.api.urls")),
    path("", include("apps.cobro.api.urls")),
    path("", include("apps.conciliacion.api.urls")),
    path("", include("apps.reportes.api.urls")),
    path("", include("apps.auditoria.api.urls")),
    path("", include("apps.notificaciones.api.urls")),
    path("", include("apps.core.api.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
