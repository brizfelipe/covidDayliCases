import json
from datetime import datetime

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from user import views as userViews
from utils import database
from .models import ConsultaAPI,CovidCases

from . import operation
from .serializer import ConsultaApiSerializer, RegisterSerializer,CovidCasesSerializer




class CovidViewSet(viewsets.ModelViewSet):
    #display all querys made by the API
    queryset = ConsultaAPI.objects.all()
    serializer_class = ConsultaApiSerializer
    
    
class CovidCasesViewSet(viewsets.ModelViewSet):
    queryset = CovidCases.objects.all()
    serializer_class = CovidCasesSerializer


@csrf_exempt
def consultaApiCovid(request):
    if request.method == 'POST':

        jsonRequest:dict = JSONParser().parse(request) 
        auth = jsonRequest['authenticate']
        informacoes = jsonRequest['informacoes']
        
        #authenticate the user sent by the API
        user = authenticate(request, username=auth['username'], password=auth['password'])

        #returns bad request if the username or password is wrong or not registered in the system
        if user is None:
            database.logAPI(status='400',message='BAD_REQUEST: Username or password not found',operation='consultaAPI',dateTime=datetime.now())
            return JsonResponse({"Mensagem": "Erro: Usuario ou senha incorreto(s)"}, status=status.HTTP_400_BAD_REQUEST)
        
        #otherwise I will authenticate the json structure and validate if all fields are correct
        else:
            idOperacao = database.createIdOperacao(auth)
            database.logAPI(status='200',message='Username autenticado',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)
            consultaApiSerializer = ConsultaApiSerializer(data=informacoes)

            #if any json field is wrong or invalid, it will return a bad request informing the error to the user
            if not consultaApiSerializer.is_valid():
                database.logAPI(status='400',message=f'BAD_REQUEST: str({consultaApiSerializer.errors})',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)
                return JsonResponse(consultaApiSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        database.logAPI(status='200',message='Serializer OK',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)

        #if everything is ok let's start the API query operation
        consultaMongo = operation.operationAPI(jsonRequest,idOperacao)

        return  JsonResponse({"Backend Challenge 2021 - Covid Daily Cases": consultaMongo }, status=status.HTTP_200_OK)

@csrf_exempt
def createLogin(request):
    if request.method == 'POST':

        jsonRequest:json = JSONParser().parse(request)
        auth = jsonRequest['authenticate']
        user = jsonRequest['authenticate']['username']
        pwd = jsonRequest['authenticate']['password']
        email = jsonRequest['authenticate']['email']
        
        registroSerializer = RegisterSerializer(data=auth)
        if not registroSerializer.is_valid():
            return JsonResponse(registroSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
        else:
            #authenticate the user sent by the API
            userAuth = authenticate(request, username=user, password=pwd)
            if userAuth is None:
                userViews.register(user=user,password=pwd,email=email)
                return userViews.register(user=user,password=pwd,email=email)

            else:
                return JsonResponse({"Messenge":"UserName already registered"},status=status.HTTP_400_BAD_REQUEST)
