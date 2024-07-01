<<<<<<< HEAD
=======

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
=======

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-39@6dkzq34v-o93@8a(((f&4$kgwq5t9l#81eh@^^!ny%!ewg6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = True

<<<<<<< HEAD
# Application definition
=======

# Application definition

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'main',  # Your main application
=======
    'main',
>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
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

ROOT_URLCONF = 'social_platform.urls'

<<<<<<< HEAD
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


=======
>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'social_platform.wsgi.application'

<<<<<<< HEAD
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
=======

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
=======

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
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

<<<<<<< HEAD
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
=======

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

<<<<<<< HEAD
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Ensure you have static files configuration
STATIC_URL = '/static/'
>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
