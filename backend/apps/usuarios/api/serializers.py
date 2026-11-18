from rest_framework import serializers

from apps.usuarios.models import Colaborador, Usuario


class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ["id", "identificacion", "nombre", "cargo", "email", "activo"]


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "username", "email", "rol", "first_name", "last_name"]
