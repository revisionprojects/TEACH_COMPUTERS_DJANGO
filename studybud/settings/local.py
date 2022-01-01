# -*- coding: utf-8 -*-
from .base import *
DEBUG = True
SECRET_KEY = '*'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'studybud.db'),
    }
}