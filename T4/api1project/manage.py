#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api1project.settings')
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api1project.settings")
>>>>>>> bb6dde2e5fb9d750dbe7c15e0c66699b5d9a21c2
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> bb6dde2e5fb9d750dbe7c15e0c66699b5d9a21c2
    main()
