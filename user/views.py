from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import status

from . import forms


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

def subscription(request):

    if request.method == 'POST':
        name    = request.POST['fName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['passWord']
        password2 = request.POST['repeatPassWord']
        
        #autenticar campos vazios 
        if not name.split():
            messages.error(request,'nome em branco ou invalido')
            return redirect('subscription') 
        
        #autenticar senha 
        elif len(password) < 8:
            messages.error(request,'Usar senha com 8 ou mais caracteres')
            return redirect('subscription') 
        
        elif not any(chr.isdigit() for chr in password):
            messages.error(request,'senha muito fraca: inserir algum numero a senha')
            return redirect('subscription') 
        
        elif not any(x.isupper() for x in password):
            messages.error(request,'senha muito fraca : inserir alguma letra maiúscula')
            return redirect('subscription') 
        
        elif password != password2:
            messages.error(request,'Senhas não conferem !')
            return redirect('subscription') 
         
        #autenticar se usuario ja tem cadastro no banco de dados 
        elif User.objects.filter(email=email).exists():
            messages.error(request,'E-Mail já cadastrado')
            return redirect('subscription')
        
        #autenticar se o userName ja tem cadastro no banco de dado
        elif User.objects.filter(username=userName).exists():
            messages.error(request,'Nome de usuario já cadastrado')
            return redirect('subscription')
      
        else:
            try:
                user = User.objects.create_user(username=name,first_name=name.split()[0],last_name=name.split()[1],email=email,password=password)
                user.save()
                messages.success(request, f'Usuário  criado com sucesso. Bem vindo {name}')
                return redirect('menu')
            except ImportError as err:
                messages.error(request,f'Erro: {err}')
    else:
        form = forms.SubscriptionForms()
        context = {'subscriptionForms':form}
        return render(request,'users/subscription.html',context)


def singIn(request):
        if request.method == 'POST':
    
            userName = request.POST['user']
            password = request.POST['passWord']
        
            if userName =="" or password == "":
                messages.error(request, 'Os campos email e senha não podem ficar em branco')
                return redirect('singin')
            
            elif User.objects.filter(email=userName).exists() or User.objects.filter(username=userName).exists():
                name = User.objects.filter(email=userName).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=name, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('menu')
                    
            else:
                messages.error(request,'Usuário não cadastrado')
                return redirect('singin') 

        else:
            form = forms.SingIn()
            context = {'singIng':form}
            return render(request,'users/singin.html',context)

def menu(request):
    pass
