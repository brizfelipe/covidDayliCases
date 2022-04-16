from django.db import models

class operacao(models.Model):
    username = models.CharField(max_length=50,null=False)
    tipoOperacao = models.CharField(max_length=50,null=False)
    dataOperacao = models.CharField(max_length=26,null=False) 
