from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from utils.database import consultaMongoDB, insertAPI, logAPI
from utils.data import montaJson,countVaiant


def operationAPI(data,idOperacao):
    try:
        #insert informacoes in datebase ConsultaAPI
        insertAPI(idOperacao=idOperacao,location=data['informacoes']['location'],date1=data['informacoes']['dataInicio'],date2=data['informacoes']['dataFinal'])
        logAPI(status='200',message='informacoes adcionadas no banco de dados',dateTime=datetime.now(),idOperacao=idOperacao)

        #Consult mongoDB
        results = consultaMongoDB(location=data['informacoes']['location'],date1=data['informacoes']['dataInicio'],date2=data['informacoes']['dataFinal'])
        logAPI(status='200',message='Consultando MongoDB',dateTime=datetime.now(),idOperacao=idOperacao)
        
        #parse mongoDB return
        variantesPossitivo = {}
        variantesNegativo = []
        numeroCasos = []
        listaVariant = []
        casosRetorno = []

        #estrutura dict de retorno
        for result in results:
            dictResult={}
           
            if result['num_sequences'] >0:
                
                dictResult['variant']= result['variant']
                dictResult['date'] = result['date']
                dictResult['num_sequences']= result['num_sequences']
                listaVariant.append(result['variant'])
                numeroCasos.append(result['num_sequences'])
                casosRetorno.append(dictResult)
                variantesPossitivo['retorno']=casosRetorno
           
            else:
                variantesNegativo.append({'variant':result['variant']})
        
        if len(variantesPossitivo) <= 0:
            logAPI(status='200',message='Solicitacao finalizada com sucesso',dateTime=datetime.now(),idOperacao=idOperacao)
            return JsonResponse({"Mensagem": "As informacoes  fornecidas de localizacao e data felizmente nao retornaram nenhum caso confirmado de infectados"}, status=status.HTTP_200_OK)            
       
        else:
            #soma o total de casos registrados
            variantesPossitivo['totalCasosConfirmado']=sum(numeroCasos)

            #agrupa e conta as variantes
            variantesPossitivo['totalCasosPorVariante'] = countVaiant(listaVariant)
            return montaJson(informacoes=data['informacoes'],dictVariantes=variantesPossitivo)
   
    except:
        logAPI(status='500',message='Erro na importacao das informacoes',dateTime=datetime.now(),idOperacao=idOperacao)
        return JsonResponse({"Mensagem": "Erro na importacao das informacoes"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
