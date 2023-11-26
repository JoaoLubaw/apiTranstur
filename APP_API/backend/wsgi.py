"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
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
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles_build', 'static'))

# Atribua a aplicação WSGI configurada ao 'app'
app = application
