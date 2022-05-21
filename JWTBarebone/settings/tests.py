import sys

from JWTBarebone.settings.default import *

DEBUG = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',  # Lightweight credentials check significantly speeds up tests.
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}


TESTING = 'test' in sys.argv[1:]
if TESTING:
    print(f'{ "="*35 }\nIn TEST Mode - Disabling Migrations\n{ "="*35 }\n')

    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    # Disabling migrations will cause TestDB created based on models only.
    # This speeds up testing a lot
    MIGRATION_MODULES = DisableMigrations()
