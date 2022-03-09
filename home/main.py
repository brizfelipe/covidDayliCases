import json
import os
from distutils.log import error

import pandas as pd
from utils import connection


def getFileCovidCases(request):
    directory = os.getcwd()
    path = os.path.join(directory,'files','covid-variants.csv')
    csvFile = pd.read_csv(path)
    jsonFile = json.loads(csvFile.to_json(orient='records'))
    connection.insertMany(jsonFile)

        
    