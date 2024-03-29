

# Python imports
from os.path import abspath, basename, dirname, join, normpath
import sys

from decouple import config, Csv
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'widget_tweaks',
    'crispy_forms',
    'compressor',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'taggit',
    'django_extensions',
    'embed_video',
    'tinymce',
    'filebrowser',

    'apps.core',
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

ROOT_URLCONF = 'config.urls'

PROJECT_TEMPLATES = [
    join(BASE_DIR, 'templates'),
]

# add apps/ to the Python path
sys.path.append(normpath(join(BASE_DIR, 'apps')))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

default_dburl = 'sqlite:///' + join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl)
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Maceio'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    join(BASE_DIR, 'src', 'theme'),
    join(BASE_DIR, 'static')
]

STATIC_ROOT = join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
        'small': {'size': (120, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
        'thumbnail': {'size': (150, 150), 'crop': True},
        'medium': {'size': (430, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
        'large': {'size': (1024, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
        'full': {'size': (1280, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
    },
}

# Messages
from django.contrib.messages import constants as messages_constants

MESSAGE_TAGS = {
    messages_constants.DEBUG: 'debug',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}

PROJECT = {
    'title': config('PROJECT_TITLE'),
    'description': "",
    'author': config('PROJECT_AUTHOR'),
    'author_url': config('PROJECT_AUTHOR_URL'),
    'maps': config('GOOGLE_KEY_MAPS'),
}

FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''

TINYMCE_DEFAULT_CONFIG = {
    'min_height': 150,
    'width': '85%',
    'height': '500px',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists charmap print
            ''',
    'toolbar1': '''
            formatselect removeformat | bold italic underline strikethrough | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap |  code | preview | fullscreen |''',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'statusbar': True
}

# auth

# LOGIN_URL = 'accounts:login'
# LOGIN_REDIRECT_URL = 'core:index'
# LOGOUT_URL = 'accounts:logout'
# AUTH_USER_MODEL = 'accounts.User'


# Email Config
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
