from django.urls import path
from .views import *

urlpatterns = [

    path('visualizar_planta/', visualizar_planta, name='visualizar_planta'),
    path('visualizar_plano_planta/<int:id>', visualizar_plano_planta, name='visualizar_plano_planta'),

]