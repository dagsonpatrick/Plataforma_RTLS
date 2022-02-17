from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EditProfileForm, EditFotoProfileForm
from .entidades.userFoto import UserFoto
from .services import usuario_service
from .models import FotoUser
import json

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('logar_usuario')
    else:
        form_usuario = UserCreationForm()
    return render(request,'user/register.html',{"form_usuario": form_usuario})

def logar_usuario(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)

            #path_foto = get_path_foto(request)
            #request.session['path_foto'] = '/media/'+str(path_foto)

            return redirect('home')
        else:
            messages.error(request,'As credenciais do usuário estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'user/login.html', {"form_login": form_login})

@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')

@login_required()
def perfil_usuario(request):
    return render(request, 'user/profile.html',{'path_foto': request.session['path_foto']})

@login_required()
def editar_senha_usuario(request):

    if request.method == "POST":
        form_usuario = PasswordChangeForm(data=request.POST,user=request.user)
        if form_usuario.is_valid():
            form_usuario.save()
            update_session_auth_hash(request,form_usuario.user)
            return redirect('home')
        else:
            messages.error(request, 'As credenciais do usuário estão incorretas')
            return redirect('perfil_usuario')
    else:
        form_usuario = PasswordChangeForm(user=request.user)
        return render(request,'user/profile.html',{"form_usuario": form_usuario,'path_foto': request.session['path_foto'] })

@login_required()
def editar_profile_usuario(request):

    if request.method == "POST":
        form_usuario = EditProfileForm(data=request.POST,instance=request.user)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
        else:
            messages.error(request, 'Todos os campos são obrigatorios')
            return redirect('perfil_usuario')
    else:
        form_usuario = EditProfileForm(instance=request.user)
        return render(request,'user/profile.html',{"form_usuario": form_usuario,'path_foto': request.session['path_foto']})

@login_required()
def cadastrar_foto_usuario(request):
    if request.method == "POST":
        form_usuario = EditFotoProfileForm(request.POST, request.FILES)
        if form_usuario.is_valid():
            foto = form_usuario.cleaned_data["foto"]
            user_foto = UserFoto(foto=foto, usuario=request.user)
            usuario_service.cadastrar_foto(user_foto)
            return redirect('home')
    else:
        form_usuario = EditFotoProfileForm()
    return render(request,'user/profile.html',{"form_usuario": form_usuario,'path_foto': request.session['path_foto']})

@login_required()
def editar_foto_usuario(request, id):
    try:
        foto_bd = usuario_service.get_usuario_foto(id)
        form_usuario = EditFotoProfileForm(request.POST, request.FILES)
        if form_usuario.is_valid():
            foto = form_usuario.cleaned_data["foto"]
            foto_nova = FotoUser(foto = foto)
            usuario_service.editar_foto(foto_bd,foto_nova)
            request.session.modified = True
            return redirect('home')
    except FotoUser.DoesNotExist:
        cadastrar_foto_usuario(request)
    return render(request, 'user/profile.html',{'path_foto': request.session['path_foto']})

@login_required()
def deletar_usuario(request, id):
    usuario_bd = usuario_service.get_usuario_id(id)
    usuario_01 = usuario_bd
    '''usuario_check = request.user.username
    if usuario_01 != usuario_check:
        return HttpResponse('Usuário logado não tem permição para essa ação')'''
    if request.method == "POST":
        usuario_service.remover_usuario(usuario_bd)
        return redirect('cadastrar_usuario')
    return render(request, 'user/confirma_exclusao_user.html',{'path_foto': request.session['path_foto']})




'''def get_path_foto(iduser):
    path = usuario_service.get_usuario_foto(iduser)
    return path.foto
def get_foto_path(request):
    path = usuario_service.get_usuario_foto(request.user.id)
    print(path.foto)
    return render(request, 'indexBase.html' )'''


