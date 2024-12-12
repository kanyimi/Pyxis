
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')

DEBUG = False

AUTH_USER_MODEL = 'chat.account'



# ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '5.255.116.253,localhost,127.0.0.1,kpyx.co,www.kpyx.co,kpyx.io,www.kpyx.io,www.krmp.io,krmp.io,2krk.site').split(',')

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '5.255.116.253,kpyx.co,www.kpyx.co,kpyx.io,www.kpyx.io,198.177.124.125').split(',')
# Добавьте CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'https://kpyx.co',
    'https://www.kpyx.co',
    "https://kpyx.io",
    "https://2krk.site",
    "https://www.kpyx.io",
    "https://www.krmp.io",
    "https://krmp.io",
    "https://localhost",
    "https://portfolio-gzbf.onrender.com",
    "https://install.kkrn.co",
    "https://krn.is",

]

# Добавьте CSRF_TRUSTED_ORIGINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'Pyxis',
    'chat',
    "admin_honeypot",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "chat.middleware.ContentSecurityPolicyMiddleware"
]

CORS_ORIGIN_ALLOW_ALL = False
SECURE_SSL_REDIRECT=False





CORS_ALLOWED_ORIGINS = [
    "https://kpyx.co",
    "https://www.kpyx.co",
    "https://185.100.87.158:8000",
    "https://localhost:8000",
    "https://0.0.0.0:8000",
    "https://kpyx.io",
    "https://www.kpyx.io",
    "https://www.krmp.io",
    "https://krmp.io",
    "https://localhost",
    "https://2krk.site",
    "https://kpyx.io",
    "https://portfolio-gzbf.onrender.com",
    "https://dkm.ac",
    "http://127.0.0.1:5500",
    "https://krn.is",
    "https://install.kkrn.co"

]

CORS_ORIGIN_WHITELIST = [
    "https://www.krmp.io",
    "https://krmp.io",
    "https://localhost",
    "https://2krk.site",
    "https://kpyx.io",
]

ROOT_URLCONF = 'Pyxis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'chat' / 'templates'],
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

WSGI_APPLICATION = 'Pyxis.wsgi.application'





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# X_FRAME_OPTIONS='ALLOWALL'


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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'chat' / 'static',  # Убедитесь, что это указывает на корректную папку со статическими файлами
]

# Директория, куда будут собраны все статические файлы
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}

import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',  # You can set this to 'INFO' for less verbosity
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',  # Logs from DEBUG level and above
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',  # Only log errors related to requests
            'propagate': False,
        },
    },
}
