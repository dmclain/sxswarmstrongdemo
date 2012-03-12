"""
Add any additional URLs that should only be available when using the the
settings.development configuration.

See ``urls.defaults`` for a list of all URLs available across both
configurations.
"""
from .defaults import *

urlpatterns += patterns('',

    # Examples:
    # url(r'^$', 'treedemo.views.debug', name='debug'),
    # url(r'^treedemo/', include('treedemo.debug.urls')),
)

# Load staticfiles for testing purposes
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
