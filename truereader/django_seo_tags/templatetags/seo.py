from django import template
from django.utils.safestring import mark_safe

from django_seo_tags.models import SeoDefault

register = template.Library()

@register.simple_tag
def common_seo_tags():
    default_seo = SeoDefault.objects.first()

    seo_tag_list = [
        '<meta name="robots" content="index, follow">',
        '<meta http-equiv="content-type" content="text/html;UTF-8">',
        '<meta http-equiv="content-security-policy" content="upgrade-insecure-requests">',
        '<meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">',
        '<meta content="IE=edge; chrome=1" http-equiv="X-UA-Compatible" />',
        '<meta name="apple-mobile-web-app-capable" content="yes">',
        '<meta name="mobile-web-app-capable" content="yes">',
        '<meta name="twitter:card" content="summary">',
    ]

    if default_seo:
        seo_tag_list.extend([
            f'<meta property="og:site_name" content="{default_seo.site_name}" />',
            f'<meta name="apple-mobile-web-app-title" content="{default_seo.site_name}">',
            f'<meta content="{default_seo.keywords}" name="keywords" itemprop="keywords" />',
            '''
            <script async src="https://www.googletagmanager.com/gtag/js?id=%s" type="text/javascript"></script>
            <script type="text/javascript">
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', "%s");
            </script>
            '''%(default_seo.google_analytics_id)
        ])

        if default_seo.twitter_handle:
            seo_tag_list.append(f'<meta name="twitter:site" content="{default_seo.twitter_handle}">')

        if default_seo.extra_tags:
            seo_tag_list.extend(default_seo.extra_tags)

    seo_tags_str = ''.join(seo_tag_list)

    return mark_safe(seo_tags_str)

@register.simple_tag(takes_context=True)
def seo_tags(context, **kwargs):
    kwargs = kwargs.get('all', kwargs)
    seo_tag_list = []
    request = context['request']
    canonical_url = request.build_absolute_uri(request.path)
    default_seo = SeoDefault.objects.first()

    title = kwargs.get('title')

    description = kwargs.get('description')

    image_url = kwargs.get('image_url')
    image_width = kwargs.get('image_width')
    image_height = kwargs.get('image_height')
    image_alt = kwargs.get('image_alt')

    theme_color = kwargs.get('theme_color')

    if default_seo:
        title = f'{title} {default_seo.seperator} {default_seo.title}'
        description = description or default_seo.description
        theme_color = theme_color or default_seo.theme_color

    if title:
        seo_tag_list.extend([
            f'<title>{title}</title>',
            f'<meta property="og:title" content="{title}" />',
            f'<meta name="twitter:title" content="{title}">',
        ])

    if description:
        seo_tag_list.extend([
            f'<meta name="description" content="{description}">',
            f'<meta name="og:description" content="{description}">',
            f'<meta name="twitter:description" content="{description}">',
        ])

    if image_url:
        image_url = request.build_absolute_uri(image_url)
        seo_tag_list.extend([
            f'<meta property="og:image" content="{image_url}" />',
            f'<meta property="og:image:secure_url" content="{image_url}" />',
            f'<meta name="twitter:image" content="{image_url}">',
        ])

    if image_width:
        seo_tag_list.extend([
            f'<meta property="og:image:width" content="{image_width}" />',
        ])

    if image_height:
        seo_tag_list.extend([
            f'<meta property="og:image:height" content="{image_width}" />',
        ])

    if image_alt:
        seo_tag_list.extend([
            f'<meta property="og:image:alt" content="{image_alt}" />',
        ])

    if theme_color:
        seo_tag_list.extend([
            f'<meta name="theme-color" content="{theme_color}" />',
        ])

    seo_tag_list.extend([
        f'<link rel="canonical" href="{canonical_url}" />',
        f'<meta property="og:url" content="{canonical_url}" />',
    ])

    return mark_safe(''.join(seo_tag_list))
