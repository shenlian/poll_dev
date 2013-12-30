# coding: UTF-8
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$','polls.views.index'),
    url(r'^(?P<poll_id>\d+)/$','polls.views.detail'),
    url(r'^(?P<poll_id>\d+)/results/$','polls.views.results'),
    url(r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),
)
