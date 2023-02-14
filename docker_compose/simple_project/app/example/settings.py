from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include
import os


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


include(
    'components/database.py',
    'components/apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/auth_password_validators.py',
)


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'