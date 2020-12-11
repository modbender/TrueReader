from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def theme_name(context):
    request = context['request']
    return '{}'.format(request.COOKIES.get('bs_theme', 'slate'))
