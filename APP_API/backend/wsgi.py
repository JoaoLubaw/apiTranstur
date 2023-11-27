# APP_API/backend/wsgi.py

import os
import sys

# Adiciona o diretório raiz do projeto ao caminho de pesquisa de módulos do Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'APP_API'))

from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
from django.conf import settings

# Obtenha o BASE_DIR do settings.py
BASE_DIR = getattr(settings, 'BASE_DIR', None)

# Verifique se BASE_DIR está definido
if BASE_DIR is None:
    raise Exception("BASE_DIR not defined in settings.py")

# Configure a aplicação WSGI
application = get_wsgi_application()

# Configure o WhiteNoise após a configuração da aplicação WSGI
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles_build'))

# Atribua a aplicação WSGI configurada ao 'app'
app = application
