from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include
from config.components import middleware
from config.components import apps
import os

load_dotenv()

include(
    'components/database.py',
    'components/apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/auth_password_validators.py',
)

INTERNAL_IPS = [
    "127.0.0.1",
]


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get('DEBUG', False)

if DEBUG:
    apps.INSTALLED_APPS += [
        "debug_toolbar",
    ]

    middleware.MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

LOCALE_PATHS = ['movies/locale']

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
