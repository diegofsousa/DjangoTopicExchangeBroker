import os
import sys
import django

import os

from django.core.wsgi import get_wsgi_application

#os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'


def ini():
	from django.core.management import call_command
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServerBroker.settings")
	application = get_wsgi_application()
	call_command('runserver')