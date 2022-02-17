from django.urls import path
from .views import *

urlpatterns = [

    path('relatorio_plano/', relatorio_plano, name='relatorio_plano'),
    path('exibir_relatorio_plano/', exibir_relatorio_plano, name='exibir_relatorio_plano'),



]