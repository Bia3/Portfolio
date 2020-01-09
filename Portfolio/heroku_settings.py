from . import settings
import django_heroku
import dj_database_url
import os

settings.DEBUG = True
settings.TEMPLATE_DEBUG = True


# Use the production secret key
settings.SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']

settings.MIDDLEWARE.append('RossDev.middleware.SSLMiddleware')

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

# settings.django_heroku.settings(locals())
