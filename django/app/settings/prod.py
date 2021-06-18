from .base import *  # noqa: F401
import os
import environ


# Set Environment Variables casting and defaults
env = environ.Env(
    SETTINGS_DEBUG=(bool, False),
    SETTINGS_SECRET_KEY=(str, "somesecretkey123"),
)
environ.Env.read_env()


SECRET_KEY = env("SETTINGS_SECRET_KEY")
DEBUG = False


ALLOWED_HOSTS = [
    "somedomain.com",  # TODO: to be defined
]


if os.getenv("GITHUB_WORKFLOW"):
    # On github actions, use a test postresql database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github-actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
else:
    # Otherwise, use a real postresql database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("SETTINGS_DB_NAME"),
            "USER": env("SETTINGS_DB_USER"),
            "HOST": env("SETTINGS_DB_HOST"),
            "PORT": env("SETTINGS_DB_PORT"),
        }
    }
