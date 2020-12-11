from django.template import loader
from django.http import HttpResponse

import inspect
from functools import wraps
from django.core.cache import cache
from django.urls import resolve

def view_cache(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        view_name = func.__name__
        view_prefix = inspect.getmodule(view).__name__
        view_hash = hash(frozenset({
            'context': context,
            'content_type': content_type,
            'status': status,
            'using': using,
        }))
        view_key = '{}.{}_{}'.format(view_prefix, view.__name__, view_hash)
        content = cache.get(view_key)
        if not content:
            content = func(request, *args, **kwargs)
            cache.set(view_key, content, None)


def render(request, template_name, context=None, content_type=None, status=None, using=None):
    """
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """
    view = resolve(request.path_info).func
    view_prefix = inspect.getmodule(view).__name__
    view_hash = hash(frozenset({
        'context': context,
        'content_type': content_type,
        'status': status,
        'using': using,
    }))
    view_key = '{}.{}_{}'.format(view_prefix, view.__name__, view_hash)
    content = cache.get(view_key)
    if not content:
        content = loader.render_to_string(template_name, context, request, using=using)
        cache.set(view_key, content, None)

    return HttpResponse(content, content_type, status)
