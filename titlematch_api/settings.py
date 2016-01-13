"""
Django settings for titlematch_api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DJANGO_DEBUG'] == 'True'

ALLOWED_HOSTS = [
    'bracketfun-api.herokuapp.com',
    'localhost',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tournament',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG
        },
    },
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    os.environ['CORS_ORIGIN']
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'accept-encoding',
    'origin',
    'authorization',
    'x-csrftoken'
)
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
)

ROOT_URLCONF = 'titlematch_api.urls'

WSGI_APPLICATION = 'titlematch_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(),
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'test.db.sqlite3')

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
