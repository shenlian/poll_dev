# coding: UTF-8
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView,ListView


urlpatterns = patterns('',
    # url(r'^$','polls.views.index'),
    # url(r'^(?P<poll_id>\d+)/$','polls.views.detail'),
    # url(r'^(?P<poll_id>\d+)/results/$','polls.views.results'),
    # url(r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'},name='auth_login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'},name='auth_logout'),
)
