from rest_framework import serializers

from apps.incapacidades.models import AlertaPlazo, ChecklistDocumental, Incapacidad, ItemChecklist, ReglaDocumental


class ItemChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemChecklist
        fields = ["id", "tipo_requerido", "estado", "documento"]


class ChecklistSerializer(serializers.ModelSerializer):
    items = ItemChecklistSerializer(many=True, read_only=True)

    class Meta:
        model = ChecklistDocumental
        fields = ["id", "completo", "items"]


class IncapacidadSerializer(serializers.ModelSerializer):
    colaborador_nombre = serializers.CharField(source="colaborador.nombre", read_only=True)
    checklist = ChecklistSerializer(read_only=True)

    class Meta:
        model = Incapacidad
        fields = "__all__"
        read_only_fields = ["estado", "remision_tardia", "fecha_limite_transcripcion", "responsable_actual"]


class IncapacidadCrearSerializer(serializers.Serializer):
    """Entrada de RF-001."""

    colaborador_id = serializers.IntegerField()
    tipo_caso = serializers.CharField()
    fecha_inicio = serializers.DateField()
    canal = serializers.CharField()
    fecha_expedicion = serializers.DateField(required=False, allow_null=True)
    fecha_remision = serializers.DateField(required=False, allow_null=True)


class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertaPlazo
        fields = "__all__"


class ReglaDocumentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReglaDocumental
        fields = "__all__"
