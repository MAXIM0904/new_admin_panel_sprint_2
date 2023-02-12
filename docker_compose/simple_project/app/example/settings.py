from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include
import os

load_dotenv()

include(
    'components/database.py',
    'components/apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/auth_password_validators.py',
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

LOCALE_PATHS = ['movies/locale']

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "static"

STATIC_ROOT = "static"

MEDIA_ROOT = "static"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
