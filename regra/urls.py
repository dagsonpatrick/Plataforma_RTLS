from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar_regra/', cadastrar_regra, name='cadastrar_regra'),

]