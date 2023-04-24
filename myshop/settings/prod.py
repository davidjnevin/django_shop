# Prodution Settings
import os
from .base import *


DEBUG = False

ADMINS = [ (os.environ.get("ADMIN_NAME"), os.environ.get("ADMIN_EMAIL")), ]

SECRET_KEY = os.environ.get("SECRET_KEY")

# ALLOWED_HOSTS = shop.project.davidnevin.net
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="0.0.0.0").split(" ")
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME", ""),  # noqa
        "USER": os.environ.get("POSTGRES_USER", "postgres"),  # noqa
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),  # noqa
        "HOST": os.environ.get("POSTGRES_HOST", ""),  # noqa
        "PORT": os.environ.get("POSTGRES_PORT", ""),
    }
}

STATIC_ROOT = "/app/static/"
STATIC_URL = "/static/"

MEDIA_ROOT = "/app/media/"
MEDIA_URL = "/media/"

# Stripe Keys
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
STRIPE_API_VERSION = config("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")

# redis settings
REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")
REDIS_DB = config("REDIS_DB")
