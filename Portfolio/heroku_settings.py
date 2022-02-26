from .settings import *
import dj_database_url
import os

DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'www.rossdev.io', 'www.rossdev.tech', 'www.rossdev.co', 'rossdev.io', 'rossdev.tech', 'rossdev.co',
    'portf-orchard.herokuapp.com', '1276.0.0.1', 'localhost'
]

# Use the production secret key
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']

# Security settings https://docs.djangoproject.com/en/3.2/topics/security/
# SSL/HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
# # Internationalization
# # https://docs.djangoproject.com/en/1.7/topics/i18n/

