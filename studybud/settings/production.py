# -*- coding: utf-8 -*-
from .base import *
import django_heroku

SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

# Configure Django App for Heroku.

django_heroku.settings(locals())