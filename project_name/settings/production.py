# for now fetch the development settings only
from .development import *

# turn off all debugging
DEBUG = False

# ##### APPLICATION CONFIGURATION #########################
INSTALLED_APPS = DEFAULT_APPS + LIBS_APPS + APPS