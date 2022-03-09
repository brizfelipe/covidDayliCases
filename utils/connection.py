import os
from pymongo import MongoClient
from datetime import datetime
from database.models import operacao
from api.models import ConsultaAPI,LogAPI

def logAPI(status,message,dateTime,idOperacao=False):
    if not idOperacao:
        idOperacao = '0'
        LogAPI.objects.create(idOperacao=None,status=status,message=message,dateTime=dateTime.strftime("%Y,%m,%d,%H,%M,%S,%f"))
    else:
        LogAPI.objects.create(idOperacao=idOperacao,status=status,message=message,dateTime=dateTime.strftime("%Y,%m,%d,%H,%M,%S,%f"))


def createIdOperacao(auth):
    now = datetime.now()
    user = auth['username']
    operacao.objects.create(username=user,tipoOperacao='API',dataOperacao=now.strftime("%Y,%m,%d,%H,%M,%S,%f"))
    return operacao.objects.latest('id')


def insertAPI(idOperacao,location,date1,date2):
    ConsultaAPI.objects.create(idOperacao=idOperacao,location=location,dataInicio=date1,dataFinal=date2)


def insertMany(jsonLoad):
    #Connection with MongoDB
    cliente = MongoClient(os.environ.get("CONNECTION_STRING"))
    db = cliente['fbrDailyCases']
    collection =  db['covidDailyCases']
    collection.insert_many(jsonLoad)

def consultaMongoDB(location,date1,date2):
    
    #Connection with MongoDB
    cliente = MongoClient(os.environ.get("CONNECTION_STRING"))
    db = cliente['fbrDailyCases']
    collection =  db['covidDailyCases']
    returnQuery = []
    for find in collection.find({'$and': [{'location': location},{'date': {'$gte': date1}},{'date': {'$lte': date2}}]}):

        returnQuery.append(find)
    
    return returnQuery
