"""
WSGI config for fakeinstagram project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/fakeinstagram/fakeinstagram'
if path not in sys.path:
    sys.path.append(path)

# Configura el entorno de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'fakeinstagram.settings'

# Activa el entorno virtual
activate_this = '/home/fakeinstagram/fakeinstagram/env/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

# Importa y activa Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()