from rest_framework import serializers
from .models import Servicio, Socio
from .models import Tarifa, SociosServicio



class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = "__all__"

class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = "__all__"

class SociosServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SociosServicio
        fields = "__all__"


class ReporteServiciosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    servicios = ServicioSerializer(many=True)


