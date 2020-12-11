from django.contrib import admin

from django_seo_tags.models import SeoDefault

@admin.register(SeoDefault)
class SeoAdmin(admin.ModelAdmin):
    pass
