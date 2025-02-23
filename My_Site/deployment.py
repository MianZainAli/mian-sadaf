from .settings import *
import dj_database_url
import django_heroku


SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

CSRF_TRUSTED_ORIGINS = [
    f'http://{host}' for host in ALLOWED_HOSTS if host
] + [
    f'https://{host}' for host in ALLOWED_HOSTS if host
]


DATABASES = {
    'default': dj_database_url.config()
}


# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME'] 
# AWS_DEFAULT_ACL = None  
# AWS_S3_FILE_OVERWRITE = False

# AWS_STATIC_LOCATION = 'static'
# AWS_MEDIA_LOCATION = 'media'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())