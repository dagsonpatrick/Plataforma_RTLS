from django.urls import path
from .views import *

urlpatterns = [

    path('visualizar_coletor/', visualizar_coletor, name='visualizar_coletor'),

]