from django.db import models


# Create your models here.

class Times(models.Model):
    nome = models.CharField(max_length=20)
    nacionalidade = models.CharField(max_length=20)
    

class Jogadores(models.Model):
    nome = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    
