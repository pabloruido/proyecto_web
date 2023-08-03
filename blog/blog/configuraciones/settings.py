
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-p&fvvx8hc@8v0^ih129hvm_i&b7bm1d64n9hf^0llox4*2krlz'


DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'usuario.Usuario'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'analistaperdonado@gmail.com'
EMAIL_HOST_PASSWORD = 'Usuariopromedioroot1976'
# Application definition

SITE_NAME = 'Mundo IA'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.posts',
    'apps.contacto',
    'apps.nosotros',
    'apps.usuario',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[
            os.path.join(os.path.dirname(BASE_DIR),'templates'),
            
],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "informatorio",
#         "USER": "root",
#         "PASSWORD": "root",
#         "HOST": "localhost",
#         "PORT": "3306",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static'),)



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'media')

import logging

# Configuración de registros (logs)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(module)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
