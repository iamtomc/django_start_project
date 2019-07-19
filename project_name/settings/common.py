# Python imports
from os.path import abspath, basename, dirname, join, normpath
import sys
from django.contrib.messages import constants as messages_constants

from decouple import config, Csv
from dj_database_url import parse as dburl

# ##### PATH CONFIGURATION ################################

# fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# the name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'staticfiles')

# collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'media')

# look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'src', 'theme'),
    join(PROJECT_ROOT, 'static'),
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

# add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))

# ##### APPLICATION CONFIGURATION #########################

# these are the apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# libs
LIBS_APPS = [
    'rest_framework',
    'widget_tweaks',
    'crispy_forms',
    'compressor',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'embed_video',
    'tinymce',
    'filebrowser',
    'active_link',
]

# apps
APPS = [
    'core',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

# Internationalization
USE_I18N = False

# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

# these persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS

# ##### DJANGO RUNNING CONFIGURATION ######################

# the default WSGI application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# the root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

# the URL for static files
STATIC_URL = '/static/'

# the URL for media files
MEDIA_URL = '/media/'

# ##### DEBUG CONFIGURATION ###############################
DEBUG = config('DEBUG', default=False, cast=bool)

# finally grab the SECRET KEY
SECRET_KEY = config('SECRET_KEY')

# ##### DATABASE CONFIGURATION ############################
default_dburl = 'sqlite:///' + join(PROJECT_ROOT, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl)
}


# LOGIN_URL = 'accounts:login'
# LOGIN_REDIRECT_URL = 'core:index'
# LOGOUT_URL = 'accounts:logout'
# AUTH_USER_MODEL = 'accounts.User'


# libs
# COMPRESS
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True

#forms

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#thumbnail
THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (120, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
        'thumbnail': {'size': (150, 150), 'crop': True},
        'medium': {'size': (430, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
        'large': {'size': (1024, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
        'full': {'size': (1280, 0), 'autocrop': True, 'crop': 'smart', 'upscale': True},
    },
}


# Messages
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


# Email Config
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')