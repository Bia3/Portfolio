"""
Django settings for Portfolio project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from . import settings
import dj_database_url
import os

settings.DEBUG = False
settings.TEMPLATE_DEBUG = True

settings.ALLOWED_HOSTS = [
    'www.rossdev.io',
    'www.rossdev.tech',
    'www.rossdev.co',
    'rossdev.io',
    'rossdev.tech',
    'rossdev.co',
    'portf-orchard.herokuapp.com',
]

# Use the production secret key
settings.SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
settings.SECURED_FIELDS_KEY = os.environ['SECURED_FIELDS_KEY']
settings.SECURED_FIELDS_HASH_SALT = os.environ['SECURED_FIELDS_HASH_SALT']

settings.DATABASE_URL = os.environ['DATABASE_URL']

# Security settings https://docs.djangoproject.com/en/3.2/topics/security/
# SSL/HTTPS
settings.SECURE_SSL_REDIRECT = True
settings.SESSION_COOKIE_SECURE = True
settings.CSRF_COOKIE_SECURE = True


settings.DATABASES = {'default': dj_database_url.config(
    default=settings.DATABASE_URL)}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
