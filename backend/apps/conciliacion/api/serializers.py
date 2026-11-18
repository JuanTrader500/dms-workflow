from rest_framework import serializers

from apps.conciliacion.models import ConciliacionContable


class ConciliacionContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConciliacionContable
        fields = "__all__"
