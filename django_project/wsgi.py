"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# sys.path.append('/home/axel/django_project/django_project')

# sys.path.append('/home/axel/django_project/venv/lib/python3.10/site-packages')


# activate_this = '/home/axel/django_project/venv/bin/activate'
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
# os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'


application = get_wsgi_application()
