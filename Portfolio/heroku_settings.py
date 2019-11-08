from . import settings
import django_heroku
import dj_database_url
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'RossDevs.apps.RossdevsConfig',
    'markdownx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

settings.DEBUG = False
settings.TEMPLATE_DEBUG = False

# Use the production secret key
settings.SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']

# # Database
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# settings.DATABASES = {
#     'default': {
#         django_heroku.settings(databases=DATABASE_URL),
#     }
# }
#
settings.DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
# # Internationalization
# # https://docs.djangoproject.com/en/1.7/topics/i18n/

settings.django_heroku.settings(locals())
