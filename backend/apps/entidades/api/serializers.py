from rest_framework import serializers

from apps.entidades.models import EntidadEPSARL, PlazoTranscripcion


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadEPSARL
        fields = "__all__"


class PlazoTranscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlazoTranscripcion
        fields = "__all__"
