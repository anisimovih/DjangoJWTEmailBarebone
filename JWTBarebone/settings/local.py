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

SIMPLE_JWT.update({
    'SIGNING_KEY': os.environ.get('SIGNING_KEY', '')
        .replace(" ", "\n", sum(c.isspace() for c in os.environ.get('SIGNING_KEY', '')) - 3)
        .replace("\n", " ", 3),
    'VERIFYING_KEY': os.environ.get('VERIFYING_KEY', '')
        .replace(" ", "\n", sum(c.isspace() for c in os.environ.get('VERIFYING_KEY', '')) - 2)
        .replace("\n", " ", 2),
})