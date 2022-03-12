from django.http import JsonResponse
from rest_framework import status
from . import main

def refreshMongoDB(request):
    if request.method == 'GET':
        main.insertMongoDB(request)
    return JsonResponse({"Mensagem": "Consulta realizada com sucesso."}, status=status.HTTP_200_OK)

def refreshPostgres(request):
    if request.method == 'GET':
        main.insertPostgres()
    return JsonResponse({"Mensagem": "Consulta realizada com sucesso."}, status=status.HTTP_200_OK)