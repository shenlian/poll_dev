# coding: UTF-8
from django.shortcuts import render_to_response
from django.shortcuts import render

def error404(request):
    """
    404 page
    """
    print "hahahhahhsadasdhadhad"
    return render(request, "errors/404.html")

def error500(request):
    """
    500 page
    """
    print "hahahhahhsadasdhadhad"
    return render(request, "errors/500.html")