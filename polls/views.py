# Create your views here.
# coding=utf-8
"""
    Author : Shenlian
    Time:2013-12-29
"""



from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators import csrf

from polls.models import Poll , Choice, Person
from polls.form import *

# detail(request=<HttpRequest object>, poll_id='23')
# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     c = {
#             'latest_poll_list':latest_poll_list
#         }
#     return render_to_response('polls/index.html',c)

# def detail(request, poll_id):
#     p = get_object_or_404(Poll,pk=poll_id)
#     return  render_to_response('polls/detail.html',{'poll':p},context_instance=RequestContext(request))

# def results(request, poll_id): 
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/results.html',{'poll':p})

def  vote(request, poll_id):
    p = get_object_or_404(Poll,pk = poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except KeyError, Choice.DoesNotExist:
        return render_to_response('polls/detail.html',{
                'poll':p,
                'error_message':"You didn't select a choice.",
            },context_instance = RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_results',args=(p.id,)))

@csrf.csrf_protect
def person(request):
    if request.POST:
        #save the existing object
        # person = Person.objects.get(pk = 5)
        # personform = PersonForm(request.POST,instance = person)
        #save new object
        personform = PersonForm(request.POST)
        if personform.is_valid():
            # person = Person()
            # person.first_name = personform.cleaned_data['first_name']
            # person.last_name = personform.cleaned_data['last_name']
            # person.shirt_size = personform.cleaned_data['shirt_size']
            # person.save()
            personform.save()
            return HttpResponse(u'数据保存成功哦！')
    else:
        personform = PersonForm()

    data = {
        'personform':personform,
    }
    return render(request,'polls/person.html',data)