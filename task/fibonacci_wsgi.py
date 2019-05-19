import os
import sys

path = '/home/PadalaSrikanth/fibonacci/task'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'task.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

