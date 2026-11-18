from rest_framework import serializers

from apps.notificaciones.models import Notificacion


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = "__all__"
        read_only_fields = ["destinatario", "incapacidad", "mensaje", "correo_enviado", "intentos_correo"]
