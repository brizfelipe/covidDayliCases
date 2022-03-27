import os
from pymongo import MongoClient
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions

class AccessPostgres:

    connectionString = os.environ.get("CONNECTION_STRING_POSTGRES")
    engine = os.environ.get("ENGINE")
    name = os.environ.get("NAME")
    user = os.environ.get("USER")
    password = os.environ.get("PASSWORD")
    host = os.environ.get("HOST")
    port = os.environ.get("PORT")


# class AccesMongoDB:

#     # connectionString = os.environ.get("CONNECTION_STRING")
#     # db_name = os.environ.get("db_name")

#     # # Establish connection with  MongoDB
#     # client = MongoClient(connectionString)

#     #  # Get codec option
#     # legOpts = CodecOptions(uuid_representation=UuidRepresentation.CSHARP_LEGACY)

#     # #Get collection
#     # collectionProposta = client.get_database(db_name).get_collection('covidDailyCases', codec_options=legOpts)


class TokenKaggle:

    token = os.environ.get("auth")
