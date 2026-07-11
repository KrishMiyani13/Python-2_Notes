"""
ASGI config for api1project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api1project.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api1project.settings")
>>>>>>> bb6dde2e5fb9d750dbe7c15e0c66699b5d9a21c2

application = get_asgi_application()
