#!D:\IDES-DEV\PycharmProjects\PlataformaUWB\venv\Scripts\python.exe
import os

from django.core.wsgi import get_wsgi_application

#import sys
#sys.path.insert(0, 'D:/IDES-DEV/PycharmProjects/PlataformaUWB/gerenciador_uwb')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador_uwb.settings')

application = get_wsgi_application()
