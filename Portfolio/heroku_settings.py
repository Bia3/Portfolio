import settings
import django_heroku
import os

settings.DEBUG = False
settings.TEMPLATE_DEBUG = False

# Use the production secret key
settings.SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# # Database
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
#
# settings.DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
# # Internationalization
# # https://docs.djangoproject.com/en/1.7/topics/i18n/

django_heroku.settings(locals())
