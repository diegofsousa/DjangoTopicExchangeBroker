import os
import sys
import django

import os

from django.core.wsgi import get_wsgi_application

#os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'
from django.core.management import call_command
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServerBroker.settings")
application = get_wsgi_application()
def start():
	call_command('runserver', '0.0.0.0:8000', '--noreload')

def stop():
	print(dir(django.core.management.find_commands))
	#django.core.management.sys.exit()

