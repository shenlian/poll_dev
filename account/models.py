#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    #This field is required
    user = models.OneToOneField(User)

    #other fields here 
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Dragons.")
    def __unicode__(self):
        return self.user.username