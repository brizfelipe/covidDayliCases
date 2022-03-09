import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from .serializer import ConsultaApiSerializer
from .operation import operationAPI
from utils.connection import createIdOperacao,logAPI
from datetime import datetime


@csrf_exempt
def consultaApiCovid(request):
    if request.method == 'POST':

        data = JSONParser().parse(request) 
        auth = data['authenticate']
        informacoes = data['informacoes']
        
        user = authenticate(request, username=auth['username'], password=auth['password'])
        if user is None:
            logAPI(status='400',message='BAD_REQUEST: Username ou password nao encontrado',dateTime=datetime.now())
            return JsonResponse({"Mensagem": "Erro: Usuario ou senha incorreto(s)"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            idOperacao = createIdOperacao(auth
            )
            logAPI(status='200',message='Username autenticado',dateTime=datetime.now(),idOperacao=idOperacao)
            consultaApiSerializer = ConsultaApiSerializer(data=informacoes)
            if not consultaApiSerializer.is_valid():
                logAPI(status='400',message=f'BAD_REQUEST: str({consultaApiSerializer.errors})',dateTime=datetime.now(),idOperacao=idOperacao)
                return JsonResponse(consultaApiSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        logAPI(status='200',message='Serializer OK',dateTime=datetime.now(),idOperacao=idOperacao)
        consultaMongo = operationAPI(data,idOperacao)

        return  JsonResponse({"Backend Challenge 2021 - Covid Daily Cases": consultaMongo }, status=status.HTTP_200_OK)
