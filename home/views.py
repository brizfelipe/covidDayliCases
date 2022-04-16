from django.http import JsonResponse
from rest_framework import status
from . import main


def refreshPostgres(request):
    if request.method == 'GET':
        main.insertPostgres()
    return JsonResponse({"Mensagem": "Consulta realizada com sucesso."}, status=status.HTTP_200_OK)