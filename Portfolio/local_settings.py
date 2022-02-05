from . import settings
import os

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

settings.SECRET_KEY = 'algzax1rw-q@syhjd1ibleuazj6_2oumyq%3ps3$$11m@29&c0'

# settings.ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.50.204']
settings.ALLOWED_HOSTS = []

settings.DEBUG = True
settings.TEMPLATE_DEBUG = True

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

