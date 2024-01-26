"""
WSGI config for compressor_configurations project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compressor_configurations.settings')
os.environ['DJANGO_CONFIGURATION'] = 'BaseConf'

application = get_wsgi_application()
