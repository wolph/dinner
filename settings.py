'''
Django settings for koornbeurs_eten project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
'''
import datetime
import decimal
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_!7kv(58rl%tu&8_r@4yrb#*^jq600wr^m57=$&sgf*=3!-ip7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = (
    'www.koornbeurs.nl',
    'www.koornbeurs.nl.',
    '.koornbeurs.nl',
    '.koornbeurs.nl.',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dinner',
    'south',
    'django_utils',
    'coffin',
    'compressor',
    'tags_input',
    'reversion',
    'koornbeurs',
    'gunicorn',
    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/dinner/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

JINJA2_EXTENSIONS = [
    'compressor.contrib.jinja2ext.CompressorExtension',
]

COMPRESS_YUI_BINARY = 'yuicompressor'
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

DEFAULT_DINNER_DAYS = 5
DEFAULT_DINNER_PRICE = decimal.Decimal('4')
DEFAULT_DINNER_COST = decimal.Decimal('2.3')
DEFAULT_DINNER_COURSES = [
    'vlees',
    'vego',
]
DINNER_SIGNUP_UNTIL = datetime.time(20)

def auth_user_queryset(*args, **kwargs):
    from koornbeurs.models import User
    return (User.objects
        .select_related('userprofiledata')
        .exclude(userprofiledata__first_name='')
        .exclude(userprofiledata__last_name='')
        .exclude(username='')
        .exclude(userprofiledata__first_name__isnull=True)
        .exclude(userprofiledata__last_name__isnull=True)
        .exclude(username__isnull=True)
    )

TAGS_INPUT_MAPPINGS = {
    'dinner.Dinner': {
        'field': 'date',
    },
    'dinner.Course': {
        'field': 'name',
        'create_missing': True,
    },
    'auth.User': {
        # NOTE! Actual queryset defined in koornbeurs.models at the bottom
        'field': 'username',
        #'fields': ('username', 'userprofiledata__first_name', 'userprofiledata__last_name'),
        #'separator': ', ',
        'queryset': auth_user_queryset,
    },
    # 'auth.User': {
    #     'fields': ('first_name', 'last_name', 'username'),
    # },
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

LOGIN_URL = '/opschepperij/aanmelden?op=auth;method=init'
LOGOUT_URL = '/opschepperij/aanmelden?op=auth;method=logout'

DJANGO_UTILS_USE_JINJA = True

INTERNAL_IPS = (
    '127.0.0.1',
)

'''Monkeypatch Django to mimic Jinja2 behaviour'''
from django.utils import safestring
if not hasattr(safestring, '__html__'):
    safestring.SafeString.__html__ = lambda self: str(self)
    safestring.SafeUnicode.__html__ = lambda self: unicode(self)

if os.path.isfile('local_settings.py'):
    execfile('local_settings.py')

if DEBUG:
    def show_toolbar(request):
        if request.META['REMOTE_ADDR'] in INTERNAL_IPS:
            return True
        elif request.user.is_staff:
            return True
        else:
            return False

    #MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += (
        'devserver',
        #'debug_toolbar',
        #'cache_toolbar',
        #'template_timings_panel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        #'template_timings_panel.panels.TemplateTimings.TemplateTimings',
        #'cache_toolbar.panels.BasePanel',
    )

    #INSTALLED_APPS += ('devserver',)
    DEVSERVER_MODULES = (
        #'devserver.modules.sql.SQLRealTimeModule',
        'devserver.modules.sql.SQLSummaryModule',
        #'devserver.modules.profile.ProfileSummaryModule',

        # Modules not enabled by default
        #'devserver.modules.ajax.AjaxDumpModule',
        'devserver.modules.profile.MemoryUseModule',
        'devserver.modules.cache.CacheSummaryModule',
        #'devserver.modules.profile.LineProfilerModule',
    )
    DEVSERVER_TRUNCATE_SQL = False
    DEVSERVER_AUTO_PROFILE = False
    DEVSERVER_DEFAULT_ADDR = '0.0.0.0'
    DEVSERVER_DEFAULT_PORT = '8080'

    import re
    import pprint
    import inspect

    pf = pprint.pformat

    def pp(*args, **kwargs):
        '''PrettyPrint function that prints both the variable name and data'''
        name = None
        for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
            m = re.search(r'\bpp\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
            if m:
                name = m.group(1)
                break

        if name:
            print '# %s:' % name
        pprint.pprint(*args, **kwargs)

else:
    pf = lambda *a, **kw: ''
    pp = lambda *a, **kw: None

import __builtin__
__builtin__.pf = pf
__builtin__.pp = pp

