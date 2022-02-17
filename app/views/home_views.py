from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from ..services import home_service
from django.core.exceptions import ObjectDoesNotExist



@login_required()
def home(request):
    set_session_path_foto(request)
    return render(request, 'indexBase.html',{'path_foto': request.session['path_foto']})

def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')

def set_session_path_foto(request):
    try:
        path = home_service.get_usuario_foto(request.user.id)
        request.session['path_foto'] = '/media/' + str(path.foto)
    except ObjectDoesNotExist:
        request.session['path_foto'] = '/media/avatar/avatar.png'
