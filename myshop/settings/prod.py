# Prodution Settings
import os
from .base import *
from decouple import config


DEBUG = True

ADMINS = [ (os.environ.get("ADMIN_NAME"), os.environ.get("ADMIN_EMAIL")), ]

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="localhost").split(" ")

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

