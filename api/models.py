from django.db import models
from database.models import operacao


class ConsultaAPI(models.Model):
    idOperacao = models.ForeignKey(operacao,on_delete=models.CASCADE)
    location = models.CharField(max_length=50,null=False)
    dataInicio = models.CharField(max_length=10,null=False)
    dataFinal = models.CharField(max_length=10,null=False)

class LogAPI(models.Model):
    idOperacao = models.ForeignKey(operacao,on_delete=models.CASCADE,null=True)
    status = models.IntegerField(null=False)
    message = models.CharField(max_length=100,null=False)
    dateTime = models.CharField(max_length=26,null=False) 

class CovidCases(models.Model):
    location = models.CharField(max_length=50,null=False)
    date = models.DateField(null=False)
    variant = models.CharField(max_length=10,null=False)
    num_sequences = models.IntegerField(max_length=100, null=False)
    perc_sequences = models.IntegerField(max_length=100, null=False)
    num_sequences_total = models.IntegerField(max_length=100, null=False)
