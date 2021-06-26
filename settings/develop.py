# -*- coding: UTF-8 -*-
"""
@Author  ：dongli
@File    ：develop.py
@Time    ：2021/6/26 18:24 
"""
from .base import * # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}