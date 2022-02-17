from django.urls import path
from .views import *

urlpatterns = [

    path('monitorar_plano/', monitorar_plano, name='monitorar_plano'),
    path('listar_plano_monitoramento/', listar_plano_monitoramento, name='listar_plano_monitoramento'),

    path('monitorar_departamento/', monitorar_departamento, name='monitorar_departamento'),
    path('listar_planos_departamento/', listar_planos_departamento, name='listar_planos_departamento'),

    path('monitorar_site/', monitorar_site, name='monitorar_site'),
    path('listar_planos_site/', listar_planos_site, name='listar_planos_site'),

]