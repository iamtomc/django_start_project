# project imports
from .common import *

LIBS_APPS += [
    'django_extensions',
]

INSTALLED_APPS = DEFAULT_APPS + LIBS_APPS + APPS
