from storages.backends.s3boto3 import S3Boto3Storage

from base import settings


class StaticStorage(S3Boto3Storage):
    location = settings.AWS_LOCATION
    default_acl = 'public-read'


static_storage = StaticStorage()
