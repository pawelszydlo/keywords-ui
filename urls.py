from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    # front
    url(r'^$', 'keywords-ui.front.views.index', name='index'),
)

# using django's static serve only for testing
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static/'}),
    )
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'media/'}),
    )
