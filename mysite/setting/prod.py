from mysite.settings import *
#py manage.py runserver --settings=mysite.setting.prod

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uju=r@mdggpolphi8=8f=mpd@_g7v-hdlu=5ufl_mi228ya7-d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://project-askari.ir','project-askari.ir']


# INSTALLED_APPS =[]

#site freamwork
SITE_ID = 3


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project3_travel',
        'USER': 'project3_iliya',
        'PASSWORD': '@1386E1386',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


STATIC_ROOT= '/home/project3/public_html/static'
MEDIA_ROOT= '/home/project3/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

CSRF_COOKIE_SECURE = True

## X-Frame-Options
X_FRAME_OPTIONS = 'SAMEPRIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 
# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'



COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
