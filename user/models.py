
from django.db import models
from database.models import operacao

class Users(models.Model):
    idOperacao = models.ForeignKey(operacao,null=False,on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)
