# noinspection PyUnresolvedReferences
from .base import *
# noinspection PyUnresolvedReferences
from .env import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
