#coding=UTF-8
from account.models import *
from django.contrib import admin

RegisterClass=(UserProfile,)
for temp in RegisterClass:
    admin.site.register(temp)