import os
from datetime import datetime

from api.models import ConsultaAPI, LogAPI

from database.models import operacao


def logAPI(status,message,operation,dateTime,idOperacao=False):
    if not idOperacao:
        idOperacao = '0'
        LogAPI.objects.create(idOperacao=None,status=status,message=message,operation=operation,dateTime=dateTime.strftime("%Y,%m,%d,%H,%M,%S,%f"))
    else:
        LogAPI.objects.create(idOperacao=idOperacao,status=status,message=message,operation=operation,dateTime=dateTime.strftime("%Y,%m,%d,%H,%M,%S,%f"))


def createIdOperacao(auth):
    now = datetime.now()
    user = auth['username']
    operacao.objects.create(username=user,tipoOperacao='API',dataOperacao=now.strftime("%Y,%m,%d,%H,%M,%S,%f"))
    return operacao.objects.latest('id')


def insertAPI(idOperacao,location,date1,date2):
    ConsultaAPI.objects.create(idOperacao=idOperacao,location=location,dataInicio=date1,dataFinal=date2)
