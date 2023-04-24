# Development settings

from decouple import Csv, config
from .base import *


SITE_ID = 1

DEBUG = True

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_FILE_STORAGE = config(
    "DEFAULT_FILE_STORAGE", default="django.core.files.storage.FileSystemStorage"
)

# Stripe Keys
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
STRIPE_API_VERSION = config("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")

# redis settings
REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")
REDIS_DB = config("REDIS_DB")
