#Jesse Fitzjarrell 9-30-15
#Blatent copying of Django Girls blog with some minor modifications. 
#I did this to learn Django and prove that I can follow a code example 
# I added a jQuery hide show on the comment section and changed the CSS 
"""
WSGI config for Capstone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Capstone.settings")

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)