from .base import *  # noqa: F401 F403


SECRET_KEY = "someFakeDevelopmentSecretKey1234"
DEBUG = True


ALLOWED_HOSTS = ["*"]


# Here for local development purposes a simple sqlite3 db is used,
# but it should probably be better to use a db that's similar to production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
