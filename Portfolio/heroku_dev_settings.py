import dj_database_url
import os

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'portdev.herokuapp.com'
]

# Use the production secret key
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
