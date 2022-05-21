"""Default settings for any environment."""

from JWTBarebone.settings.default import *

DEBUG = True

SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}