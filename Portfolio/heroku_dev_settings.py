import dj_database_url
import os

DEBUG = True
TEMPLATE_DEBUG = True

# ToDo: Finish setting up Heroku Allowed Hosts for Dev
# ALLOWED_HOSTS = [
#     '127.0.0.1', 'localhost', 'portdev.herokuapp.com'
# ]
ALLOWED_HOSTS = ['*']
# Use the production secret key
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Security settings https://docs.djangoproject.com/en/3.2/topics/security/
# SSL/HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
