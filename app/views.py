from django.shortcuts import render
from rest_framework import viewsets 
from .models import * 
from .serializers import *
# Create your views here.

class TimesView(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimeSerializers

class JogadoresView(viewsets.ModelViewSet):
    queryset = Jogadores.objects.all()
    serializer_class = JogadoresSerializers