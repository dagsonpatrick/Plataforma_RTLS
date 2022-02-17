from django.shortcuts import render
from .services import coletor_service
# Create your views here.
def visualizar_coletor(request):
    coletor_bd = coletor_service.listar_coletor()
    return render(request, 'coletor/form_listar_coletor.html', {'coletores': coletor_bd, 'path_foto': request.session['path_foto']})