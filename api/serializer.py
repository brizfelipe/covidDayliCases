from rest_framework import serializers
from .models import ConsultaAPI,Register,CovidCases

class ConsultaApiSerializer(serializers.ModelSerializer):

    class Meta:
        model=ConsultaAPI
        fields=[
            'location',
            'dataInicio',
            'dataFinal',
        ]

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=Register
        fields=[
            'username',
            'password',
            'email',
        ]
class CovidCasesSerializer(serializers.ModelSerializer):
      class Meta:
          model = CovidCases
          fields=[
              'location',
              'date',
              'variant',
              'num_sequences',
              'perc_sequences',
              'num_sequences_total',
              
          ]

