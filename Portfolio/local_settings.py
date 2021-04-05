from . import settings
import os

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

settings.ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.50.204']

settings.DEBUG = True

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

