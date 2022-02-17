"""gerenciador_uwb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('',include('accounts.urls')),
    path('',include('planos.urls')),
    path('',include('tag.urls')),
    path('',include('anchor.urls')),
    path('',include('collaborator.urls')),
    path('',include('associar.urls')),
    path('',include('monitor.urls')),
    path('',include('coletor.urls')),
    path('api/',include('api.urls')),
    path('',include('relatorio.urls')),
    path('',include('ativo.urls')),
    path('',include('alarme.urls')),
    path('',include('visualizacao.urls')),
    path('',include('mio.urls')),
    path('',include('regra.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
