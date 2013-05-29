from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.simple import direct_to_template
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    
    # Favicon
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL + 'img/favicon.ico'}),

    # Robots.txt
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 
    										'mimetype': 'text/plain',
    										'extra_context': {"env": os.environ['DJANGO_SETTINGS_MODULE'].split(".")[2]}}),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),

    
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns