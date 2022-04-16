from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from utils import database,data,query

def operationAPI(json,idOperacao):
    try:
        #insert informacoes in datebase ConsultaAPI
        database.insertAPI(idOperacao=idOperacao,location=json['informacoes']['location'],date1=json['informacoes']['dataInicio'],date2=json['informacoes']['dataFinal'])
        database.logAPI(status='200',message='informacoes adcionadas no banco de dados',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)

        #query Postgres
        results = query.Postgres.consultaAPI(location=json['informacoes']['location'],date1=json['informacoes']['dataInicio'],date2=json['informacoes']['dataFinal'])
        if results == -1:
            database.logAPI(status='500',message='Unexpected error in query in Postgres database',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)        
        else:
            database.logAPI(status='200',message='query performed successfully',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)
        
        #parse mongoDB return
        variantesPossitivo = {}
        variantesNegativo = []
        numeroCasos = []
        listaVariant = []
        casosRetorno = []

        #structure dict the retorno
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
            database.logAPI(status='200',message='Solicitacao finalizada com sucesso',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)
            return JsonResponse({"Mensagem": "As informacoes  fornecidas de localizacao e data felizmente nao retornaram nenhum caso confirmado de infectados"}, status=status.HTTP_200_OK)            
       
        else:
            #sum the total number of confirmed cases
            variantesPossitivo['totalCasosConfirmado']=sum(numeroCasos)

            #group and count the overall of variants
            variantesPossitivo['totalCasosPorVariante'] = data.countVaiant(listaVariant)
            return data.montaJson(informacoes=json['informacoes'],dictVariantes=variantesPossitivo)
   
    except:
        database.logAPI(status='500',message='Erro na importacao das informacoes',operation='consultaAPI',dateTime=datetime.now(),idOperacao=idOperacao)
        return JsonResponse({"Mensagem": "Erro na importacao das informacoes"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
