# Prodution Settings
import os
from .base import *


DEBUG = False

ADMINS = [ (os.environ.get("ADMIN_NAME"), os.environ.get("ADMIN_EMAIL")), ]

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = shop.project.davidnevin.net
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

