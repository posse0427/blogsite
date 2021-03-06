from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = '3xr*n=s20s=^2p)(n3fqo=1ymtl96kvd_23lfsokkc7jxepj@-'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar',
]

try:
    from .local import *
except ImportError:
    pass
