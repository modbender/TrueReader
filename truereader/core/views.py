from django.shortcuts import render

from . import models, forms

def home(request):
    comics = models.Comic.objects.all()
    comic_form = forms.ComicForm(request.POST or None, request.FILES or None)
    return render(request, 'core/home.html', {'comics': comics, 'comic_form': comic_form})
