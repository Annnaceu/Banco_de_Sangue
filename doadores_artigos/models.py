from django.db import models
from django.utils import timezone

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    tipo_sanguineo = models.CharField(max_length=3)
    data_ultima_doacao = models.DateField(default=timezone.now) 
    data_donacao = models.DateField()  
