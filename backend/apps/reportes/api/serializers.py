from rest_framework import serializers

from apps.reportes.models import ReporteAusentismo


class ReporteAusentismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteAusentismo
        fields = "__all__"
