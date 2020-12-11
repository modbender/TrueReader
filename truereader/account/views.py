from django.shortcuts import render
from django.http import HttpResponse, Http404

def change_theme(request):
    theme_name = request.POST.get('theme_name')
    if theme_name:
        response = HttpResponse(status=200)
        response.set_cookie('bs_theme', theme_name)
        return response
    raise Http404
