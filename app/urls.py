from django.conf import settings
from rest_framework import routers
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register(r'times', TimesView)
router.register(r'jogadores', JogadoresView)
urlpatterns = []
urlpatterns += router.urls