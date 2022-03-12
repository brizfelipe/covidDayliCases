import json
from datetime import datetime

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from utils import database

from . import operation
from .serializer import ConsultaApiSerializer


@csrf_exempt
def consultaApiCovid(request):
    if request.method == 'POST':

        jsonRequest:json = JSONParser().parse(request) 
        auth = jsonRequest['authenticate']
        informacoes = jsonRequest['informacoes']
        
        #authenticate the user sent by the API
        user = authenticate(request, username=auth['username'], password=auth['password'])

        #returns bad request if the username or password is wrong or not registered in the system
        if user is None:
            database.logAPI(status='400',message='BAD_REQUEST: Username ou password nao encontrado',dateTime=datetime.now())
            return JsonResponse({"Mensagem": "Erro: Usuario ou senha incorreto(s)"}, status=status.HTTP_400_BAD_REQUEST)
        
        #otherwise I will authenticate the json structure and validate if all fields are correct
        else:
            idOperacao = database.createIdOperacao(auth)
            database.logAPI(status='200',message='Username autenticado',dateTime=datetime.now(),idOperacao=idOperacao)
            consultaApiSerializer = ConsultaApiSerializer(jsonRequest=informacoes)

            #if any json field is wrong or invalid, it will return a bad request informing the error to the user
            if not consultaApiSerializer.is_valid():
                database.logAPI(status='400',message=f'BAD_REQUEST: str({consultaApiSerializer.errors})',dateTime=datetime.now(),idOperacao=idOperacao)
                return JsonResponse(consultaApiSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        database.logAPI(status='200',message='Serializer OK',dateTime=datetime.now(),idOperacao=idOperacao)

        #if everything is ok let's start the API query operation
        consultaMongo = operation.operationAPI(jsonRequest,idOperacao)

        return  JsonResponse({"Backend Challenge 2021 - Covid Daily Cases": consultaMongo }, status=status.HTTP_200_OK)
