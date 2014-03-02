from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

handler404 = 'backend.errorviews.error404'
handler500 = 'backend.errorviews.error500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','home.views.index'),
    url(r'^email/$','home.views.email'), 
    url(r'^uploadfile/$','home.views.uploadfile'),
    url(r'^polls/',include('polls.urls'),),
    url(r'^registration/',include('registration.urls'),),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# for develop to serve user-upload content in MEDIA_ROOT
# if settings.DEBUG:
#     urlpatterns += patterns('',
#             url(r'^media/(?P<path>.*)$',
#                 'django.views.static.serve',
#                 {'document_root': settings.MEDIA_ROOT}),
#                 )

