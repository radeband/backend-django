import os
from pathlib import Path

from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd parties
    'rest_framework',
    'django_cleanup.apps.CleanupConfig',
    'drf_yasg',
    'storages',

    # apps
    'company'
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

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='Asia/Tehran')

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# S3 Storage
S3_PROVIDER = config("S3_PROVIDER")
AWS_ACCESS_KEY_ID = config(f"{S3_PROVIDER}_S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = config(f"{S3_PROVIDER}_S3_SECRET_KEY")
AWS_S3_ENDPOINT_URL = config(f"{S3_PROVIDER}_S3_ENDPOINT_URL")
AWS_STORAGE_BUCKET_NAME = config(f"{S3_PROVIDER}_S3_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f'{config("S3_CUSTOM_DOMAIN")}/{AWS_STORAGE_BUCKET_NAME}'
AWS_LOCATION = 'static'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = '_helpers.storages.static_storage.StaticStorage'

# media
DEFAULT_FILE_STORAGE = '_helpers.storages.media_storage.MediaStorage'


# SMS
TIME_OTP_EXPIRE_INTERVAL = 5
SMS_SECRET_KEY = config('SMS_SECRET_KEY')
SMS_PROVIDER = config('SMS_PROVIDER')

GHASEDAK_URL = config('GHASEDAK_URL')
GHASEDAK_KEY = config('GHASEDAK_KEY')
GHASEDAK_SENDER = config('GHASEDAK_SENDER')