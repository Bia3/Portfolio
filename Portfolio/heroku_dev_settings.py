import dj_database_url
import os

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'www.rossdev.io', 'www.rossdev.tech', 'www.rossdev.co', 'rossdev.io', 'rossdev.tech', 'rossdev.co',
    'https://portdev.herokuapp.com/'
]

# Use the production secret key
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
