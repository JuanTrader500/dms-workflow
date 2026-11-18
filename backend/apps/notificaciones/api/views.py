from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.notificaciones.models import Notificacion

from .serializers import NotificacionSerializer


class NotificacionViewSet(ReadOnlyModelViewSet):
    """Cada usuario ve solo sus notificaciones."""

    serializer_class = NotificacionSerializer

    def get_queryset(self):
        return Notificacion.objects.filter(destinatario=self.request.user)

    @action(detail=True, methods=["post"], url_path="leer")
    def leer(self, request, pk=None):
        notificacion = self.get_object()
        notificacion.leida = True
        notificacion.save(update_fields=["leida", "actualizado_en"])
        return Response({"leida": True})
