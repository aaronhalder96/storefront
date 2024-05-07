from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-7m%ht-h#0ij#fvrzb@+ruig8jxawiu_!4#(hgxcedk#&ee8+5h'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Ab112233'
    }
}