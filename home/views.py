# Create your views here.
#coding : UTF-8
"""
    Author : Shenlian
    Time:2013-1-25
"""
from django.shortcuts import render_to_response,get_object_or_404 ,render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators import csrf
from django.contrib.auth.decorators import login_required
# Imaginary function to handle an uploaded file.
from backend.utility import handle_uploaded_file
from polls.form import *
from polls.models import * 
from django.conf import settings

def index(request):
    # request.session['member_id'] = 123
    # print 'haha'
    # print request.session['member_id']
    return render_to_response('home/index.html',context_instance=RequestContext(request))

@csrf.csrf_protect
def uploadfile(request):
    # print request.session['member_id']
    if request.method=="POST":
        uploadform=UpLoadPicForm(request.POST,request.FILES)
        if uploadform.is_valid():
            storePic(request.FILES)
            print request.POST['title']
            return HttpResponseRedirect('/polls/')
    else: 
        uploadform=UpLoadPicForm()
    return render_to_response('home/upload.html',{"uploadform":uploadform,},context_instance=RequestContext(request))

def storePic(fileobj):
    newdoc=Pic(pic=fileobj["pic"])
    newdoc.save()

@login_required
@csrf.csrf_protect
def email(request):
    print request.user
    if request.user.is_authenticated():
        print 'logined success'
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        recipients = []
        if contactform.is_valid():
            subject = contactform.cleaned_data['subject']
            message = contactform.cleaned_data['message']
            sender = contactform.cleaned_data['sender']
            recipients.append(sender)
            print subject
            print message
            print sender
            print recipients
            from django.core.mail import send_mail
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
            return HttpResponse('send mail success')
    else:
        contactform = ContactForm()

    data = {
        "contactform":contactform,
    }
    return render(request,'home/email.html',data)
