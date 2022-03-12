import json
import os
from distutils.log import error

import pandas as pd
from utils import database,files


def insertMongoDB(request):
    directory = os.getcwd()
    path = os.path.join(directory,'files','covid-variants.csv')
    csvFile = pd.read_csv(path)
    jsonFile = json.loads(csvFile.to_json(orient='records'))
    database.insertMany(jsonFile)

def insertPostgres():
    directory = os.getcwd()
    path = os.path.join(directory,'files')
    pathEntrada = os.path.join(directory,'files','covid-variants.csv')
    covidCases:list = files.readCSV(pathEntrada)
    files.saveCSVFile(path,nameFile='copy_covid-variants.csv',fileLista=covidCases)
    database.runCopyCSVCommand(os.path.join(path,'copy_covid-variants.csv'),"api_covidcases",sep=',',columns=['location','date','variant','num_sequences','perc_sequences','num_sequences_total'])

        
    