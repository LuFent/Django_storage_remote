import os
import dj_database_url
from environs import Env


env = Env()
env.read_env()

DEBUG = env.bool('DEBUG', False)

DATABASES = dict()
DATABASES["default"] = dj_database_url.parse(env('DB_URL'))

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
