from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
		return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()

	def __unicode__(self):
		return self.choice


class Person(models.Model):


    SHIRT_SIZES = (
        (u'S', u'Small'),
        (u'M', u'Medium'),
        (u'L', u'Large'),
    )
    
    first_name = models.CharField("Person first name",max_length=30)
    last_name = models.CharField(max_length=30)

    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)

    def __unicode__(self):
        return self.first_name +'-'+self.last_name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __unicode__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __unicode__(self):
        return self.group.name + '---' + self.person.first_name