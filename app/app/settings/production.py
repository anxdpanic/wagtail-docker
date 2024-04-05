from .base import *
from .env import *

DJANGO_ROOT = '/home/app/'

try:
    from .local import *
except ImportError:
    pass
