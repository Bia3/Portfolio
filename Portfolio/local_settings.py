"""
Django settings for Portfolio project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from . import settings
import os

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

SECURED_FIELDS_KEY = os.environ['SECURE_FIELDS_KEY']
SECURED_FIELDS_HASH_SALT = os.environ['SECURED_FIELDS_HASH_SALT']

ALLOWED_HOSTS = []

DEBUG = True
TEMPLATE_DEBUG = True

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}
