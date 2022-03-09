from django.http import JsonResponse
from rest_framework import status
from . import main

def index(request):
    if request.method == 'GET':
        main.getFileCovidCases(request)
    return JsonResponse({"Mensagem": "Consulta realizada com sucesso."}, status=status.HTTP_200_OK)