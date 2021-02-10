import dj_database_url
from osm.settings import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

DATABASES['default'] = dj_database_url.config(conn_max_age=500)

ALLOWED_HOSTS = ['reparepc.herokuapp.com']

SECURE_SSL_REDIRECT = True
