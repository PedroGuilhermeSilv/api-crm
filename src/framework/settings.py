import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-%j2fp=o02(+j7g+ry4hu8b9iwa^(%0gdye+2+z*p&#h834_+bd"


DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_REPLACE_HTTPS_REFERER = True
CSRF_TRUSTED_ORIGINS = ["http://*", "https://*"]
CORS_ALLOW_HEADERS = [
    "accept",
    "referer",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-sessionid",
    "x-requested-with",
]
CORS_EXPOSE_HEADERS = ["Set-Cookie"]


AUTH_USER_MODEL = "user.User"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "src.core.user.infra.django",
    "src.core.product.infra.django",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.framework.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.framework.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
    if DEBUG
    else {
        "default": {
            "ENGINE": "django_cockroachdb",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        },
    }
)


def monkeypatch_ninja_uuid_converter() -> None:
    import importlib
    import sys

    import django.urls

    module_name = "ninja.signature.utils"
    sys.modules.pop(module_name, None)

    original_register_converter = django.urls.register_converter

    def fake_register_converter(*_: Any, **__: Any) -> None:
        pass

    django.urls.register_converter = fake_register_converter
    importlib.import_module(module_name)

    django.urls.register_converter = original_register_converter


monkeypatch_ninja_uuid_converter()

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "framework/static"
STATIC_ROOT = BASE_DIR / "framework/staticfiles"
