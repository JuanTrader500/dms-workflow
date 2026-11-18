from rest_framework import serializers

from apps.cobro.models import SeguimientoCobro, ReconocimientoEconomico, RequerimientoCobro, EscalamientoCartera, GestionJuridica


class SeguimientoCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoCobro
        fields = "__all__"


class ReconocimientoEconomicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReconocimientoEconomico
        fields = "__all__"


class RequerimientoCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequerimientoCobro
        fields = "__all__"


class EscalamientoCarteraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalamientoCartera
        fields = "__all__"


class GestionJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestionJuridica
        fields = "__all__"
