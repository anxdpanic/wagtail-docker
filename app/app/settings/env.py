import os

# Wagtail settings
WAGTAIL_SITE_NAME = os.environ.get("SITE_NAME")

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.environ.get("BASE_URL")
WAGTAILADMIN_BASE_URL = os.environ.get("BASE_URL")

# Django settings
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "en-us")
TIME_ZONE = os.environ.get("TIME_ZONE", "UTC")

# Database PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),
        'NAME': os.environ.get("SQL_DATABASE"),
        'USER': os.environ.get("SQL_USER"),
        'PASSWORD': os.environ.get("SQL_PASSWORD"),
        'HOST': os.environ.get("SQL_HOST"),
        'PORT': os.environ.get("SQL_PORT"),
    }
}
