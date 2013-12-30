# Create your views here.
#coding = UTF-8
"""
    Author : Shenlian
    Time:2013-12-29
"""
from polls.models import Poll
from django.shortcuts import render_to_response,get_object_or_404
from django.http import Http404

# detail(request=<HttpRequest object>, poll_id='23')
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    c = {
            'latest_poll_list':latest_poll_list
        }
    return render_to_response('polls/index.html',c)

def detail(request, poll_id):
    # try :
    #     p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    p = get_object_or_404(Poll,pk=poll_id)
    return  render_to_response('polls/detail.html',{'poll':p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)