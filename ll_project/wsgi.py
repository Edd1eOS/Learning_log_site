""" 
WSGI config for ll_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application#wsgi是Web Server Gateway Interface的缩写，是Python Web应用程序和Web服务器之间的接口规范

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

application = get_wsgi_application()
