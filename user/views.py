from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status


def register(user,password,email):
    
    #fields void autenticar 
    if not user.split():
        return JsonResponse({"Message": "Erro: username field void)"}, status=status.HTTP_400_BAD_REQUEST)
    if not password.split():
        return JsonResponse({"Message": "Erro: username field void)"}, status=status.HTTP_400_BAD_REQUEST)
    if not email.split():
        return JsonResponse({"Message": "Erro: username field void)"}, status=status.HTTP_400_BAD_REQUEST)
    #autenticar senha 
    if len(password) < 8:
        return JsonResponse({"Message": "Very weak password: minimum 8 characters"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not any(chr.isdigit() for chr in password):
        return  JsonResponse({"Message": "Very weak password: minimum 8 characters"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not any(x.isupper() for x in password):
        return JsonResponse({"Message": "Please password must be at least one upper case"}, status=status.HTTP_400_BAD_REQUEST) 
    
    #autenticar se usuario ja tem cadastro no banco de dados 
    if User.objects.filter(email=email).exists():
        return JsonResponse({"Message": "Please password must be at least one upper case"}, status=status.HTTP_400_BAD_REQUEST) 
    
    user = User.objects.create_user(username=user,email=email,password=password)
    user.save()
