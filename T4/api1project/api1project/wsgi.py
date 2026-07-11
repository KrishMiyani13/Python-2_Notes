"""
WSGI config for api1project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api1project.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api1project.settings")
>>>>>>> bb6dde2e5fb9d750dbe7c15e0c66699b5d9a21c2

application = get_wsgi_application()
