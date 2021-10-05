import os
import sys
 
sys.path.append('/home/c/ca21350/django_3/public_html/baydibek_smartgid') # путь до проекта django; u и user - первая буква Вашего логина и сам логин соответственно
sys.path.append('/home/c/ca21350/django_3/env/lib/python3.6/site-packages/') # путь до django; u и user - первая буква Вашего логина и сам логин соответственно
os.environ['DJANGO_SETTINGS_MODULE'] = 'smartgid.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
