from rest_framework import serializers
from .models import *

class TimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Times
        fields = ["id", "nome", "nacionalidade"]

class JogadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jogadores
        fields = ["id", "nome", "time"]
        
