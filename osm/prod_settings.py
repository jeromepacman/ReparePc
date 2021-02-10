from osm.settings import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES['default'] = dj_database_url.config(conn_max_age=500)

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT = True
