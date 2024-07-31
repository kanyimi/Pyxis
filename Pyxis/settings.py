
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

AUTH_USER_MODEL = 'chat.account'

# DEBUG = True
# ALLOWED_HOSTS = ["*"]

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '185.100.87.158,localhost,kpyx.co,www.kpyx.co,kpyx.io,www.kpyx.io,www.krmp.io,krmp.io,localhost,2krk.site,').split(',')

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
]

CORS_ORIGIN_ALLOW_ALL = True



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

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# settings.py
X_FRAME_OPTIONS = 'ALLOWALL'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
