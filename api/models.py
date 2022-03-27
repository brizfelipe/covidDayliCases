from statistics import mode
from django.db import models
from database.models import operacao


class ConsultaAPI(models.Model):
    idOperacao = models.ForeignKey(operacao,on_delete=models.CASCADE)
    location = models.CharField(max_length=50,null=False)
    dataInicio = models.CharField(max_length=10,null=False)
    dataFinal = models.CharField(max_length=10,null=False)
    

class LogAPI(models.Model):
    idOperacao = models.ForeignKey(operacao,on_delete=models.CASCADE,null=True)
    operation =  models.CharField(max_length=50,null=False)
    status = models.IntegerField(null=False)
    message = models.CharField(max_length=100,null=False)
    dateTime = models.CharField(max_length=26,null=False) 
    

class CovidCases(models.Model):
    location = models.CharField(max_length=50,null=False)
    date = models.DateField(null=False)
    variant = models.CharField(max_length=20,null=False)
    num_sequences = models.IntegerField(null=False)
    perc_sequences = models.DecimalField(max_digits=10,decimal_places=2, null=False)
    num_sequences_total = models.IntegerField(null=False)
    

class Register(models.Model):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    

class returnConsultaCases(models.Model):
    pass
