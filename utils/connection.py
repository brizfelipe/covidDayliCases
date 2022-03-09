import os
from pymongo import MongoClient
from datetime import datetime
from database.models import operacao
from api.models import ConsultaAPI,LogAPI
import psycopg2

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


def runCopyCSVCommand(filepath, tableName, sep, columns=[]):

    # Connection to database
    conn = psycopg2.connect(os.environ.get("CONNECTION_STRING_POSTGRES"))
    conn.autocommit = False
    cursor = conn.cursor()
    columnsCorrigido=[]
    with open(filepath) as f:
        try:
            if len(columns) == 0:
                columns = ''
            else:
                for column in columns:
                    columnsCorrigido.append('"'+column+'"')
                    
                columns = '(' + ','.join(columnsCorrigido) + ')'

            cursor.copy_expert('copy public.' + tableName + ' ' + columns + ' from stdin with csv delimiter as ' + "\'" + sep + "\'" + " encoding \'utf-8\' ", f)

        except psycopg2.DatabaseError as err:
            conn.rollback()
            return print('Base import error : '+str(err))

    conn.commit()
    cursor.close()
    conn.autocommit = True
    return  print(f'successfully imported base: {tableName}')