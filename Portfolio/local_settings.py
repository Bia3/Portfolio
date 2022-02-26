from . import settings
import os

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# settings.ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.50.204']
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
