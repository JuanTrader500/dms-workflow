from rest_framework import serializers

from apps.auditoria.models import AuditoriaGestion


class AuditoriaGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaGestion
        fields = "__all__"
