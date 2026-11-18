from rest_framework import serializers

from apps.documentos.models import DocumentoSoporte


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoSoporte
        fields = [
            "id", "incapacidad", "nombre_archivo", "formato", "tipo_documento",
            "es_clinico", "destruido", "creado_en",
        ]
        read_only_fields = ["formato", "es_clinico", "destruido"]
