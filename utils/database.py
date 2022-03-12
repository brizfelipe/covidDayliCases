import os
from datetime import datetime

import psycopg2
from api.models import ConsultaAPI, LogAPI


from database.models import operacao

from . import connection


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
    connection.AccesMongoDB.collectionCodivDailyCases.insert_many(jsonLoad)


def consultaMongoDB(location,date1,date2):
    
    returnQuery:list = []

    #query
    query:dict = {'location': location}
    filter1:dict = {'date': {'$gte': date1}}
    filter2:dict = {'date': {'$lte': date2}}
    for find in connection.AccesMongoDB.collectionCodivDailyCases.find({'$and': [query,filter1,filter2]}):
        returnQuery.append(find)
    
    return returnQuery


def runCopyCSVCommand(filepath, tableName, sep, columns=False):

    # Connection to database
    conn = psycopg2.connect(connection.AccessPostgres.connectionString)
    conn.autocommit = False
    cursor = conn.cursor()
    columnsCorrigido:list = []

    with open(filepath) as f:
        try:
            if not columns or len(columns) == 0:
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
