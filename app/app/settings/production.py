# noinspection PyUnresolvedReferences
from .base import *
# noinspection PyUnresolvedReferences
from .env import *

DJANGO_ROOT = '/home/app/'

try:
    from .local import *
except ImportError:
    pass
