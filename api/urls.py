from django.urls import path, include
from .views import evento_view
from .views import dev_view

urlpatterns = [

    path('eventos/',evento_view.EventoList.as_view(), name='evento-list'),
    path('eventos/<int:id>', evento_view.EventoDetalhes.as_view(), name='evento-detalhes'),

    path('devs/',dev_view.DevList.as_view(), name='dev-list'),
    path('devs/<int:id>', dev_view.DevDetalhes.as_view(), name='dev-detalhes'),

    path('controller/', dev_view.DevDetalhes.as_view(), name='dev-data'),

]