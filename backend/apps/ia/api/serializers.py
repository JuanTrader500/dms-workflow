from rest_framework import serializers

from apps.ia.models import DatosExtraidos


class DatosExtraidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExtraidos
        fields = "__all__"
        read_only_fields = [f.name for f in DatosExtraidos._meta.fields]
