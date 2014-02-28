# coding=utf-8 
from django import forms
from django.forms.widgets import *
from backend.utility import validate_fize
from polls.models import *

class UpLoadPicForm(forms.Form):
    title=forms.CharField(max_length=100,help_text='Your name')
    # pic=forms.FileField(validators=[validate_fize])
    pic=forms.FileField()

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,label=u"主题",initial='Your subject')
    message = forms.CharField(label=u'信息')
    sender = forms.EmailField(label=u'收件人')
    cc_myself = forms.BooleanField(required=False,label=u'是否抄送')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person