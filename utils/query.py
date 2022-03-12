import psycopg2
from django.http import JsonResponse
from rest_framework import status

from . import connection


class MongoDB:

    def consultaMongoDB(location,date1,date2):
        
        returnQuery:list = []

        #query
        query:dict = {'location': location}
        filter1:dict = {'date': {'$gte': date1}}
        filter2:dict = {'date': {'$lte': date2}}
        for find in connection.AccesMongoDB.collectionCodivDailyCases.find({'$and': [query,filter1,filter2]}):
            returnQuery.append(find)
        
        return returnQuery

class Postgres:
    
    def consultaAPI(location,date1,date2):
        #connection with postgres
        conn = psycopg2.connect(connection.AccessPostgres.connectionString)
        cursor= conn.cursor()

        consultaAPI = f"""
            select 
                c.*
            from public.api_covidcases as c
                where 
                    c.location =  '{location}'
                and
                    c.date between  '{date1}' and '{date2}'
        """

        try:
            cursor.execute(consultaAPI)
            retorno:dict = cursor.fetchall()
       
        except:
            return -1
       
        return retorno
