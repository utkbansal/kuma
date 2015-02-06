from kuma.settings.common import *  # noqa

BANISH_ENABLED = False

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = 'memory'

ES_URLS = ['localhost:9200']
ES_INDEX_PREFIX = 'mdn'
ES_INDEXES = {'default': 'main_index'}
ES_INDEXING_TIMEOUT = 30
ES_LIVE_INDEX = True
ES_DISABLED = False

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)

INSTALLED_APPS += (
    'kuma.actioncounters.tests',
    'kuma.core.tests.taggit_extras',
)
