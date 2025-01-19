import os

from django.http import HttpResponsePermanentRedirect
from .settings import *
import dj_database_url
import django_heroku

django_heroku.settings(locals())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'mianzain-blog-eee53e8a6b0e.herokuapp.com',
    'blog.mianzain.tech',
]

DEBUG = False

MIDDLEWARE = [
    'My_Site.deployment.WWWRedirectMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
 
DATABASES = {
    'default': dj_database_url.config()
}



AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME'] 
AWS_DEFAULT_ACL = None  
AWS_S3_FILE_OVERWRITE = False

AWS_STATIC_LOCATION = 'static'
AWS_MEDIA_LOCATION = 'media'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
