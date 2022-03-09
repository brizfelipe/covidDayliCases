from rest_framework import serializers
from .models import ConsultaAPI

class ConsultaApiSerializer(serializers.ModelSerializer):

    class Meta:
        model=ConsultaAPI
        fields=[
            'location',
            'dataInicio',
            'dataFinal',
        ]

