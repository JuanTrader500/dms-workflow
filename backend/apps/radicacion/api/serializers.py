from rest_framework import serializers

from apps.radicacion.models import Radicacion


class RadicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radicacion
        fields = "__all__"
