import os

from utils import database 


class AccessPostgres:

    connectionString = os.environ.get("CONNECTION_STRING_POSTGRES")
    engine = os.environ.get("ENGINE")
    name = os.environ.get("NAME")
    user = os.environ.get("USER")
    password = os.environ.get("PASSWORD")
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")


class AccesMongoDB:

    connectionString = os.environ.get("CONNECTION_STRING")
    database = connectionString['fbrDailyCases']

    collectionCodivDailyCases = database['covidDailyCases']    

class TokenKaggle:

    token = os.environ.get("auth")
