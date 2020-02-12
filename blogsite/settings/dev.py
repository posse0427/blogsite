from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
