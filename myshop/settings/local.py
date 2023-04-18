# Setting - Dev environment

from decouple import Csv, config
from .base import *


DEBUG = True

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("DEV_ALLOWED_HOSTS", cast=Csv())

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
