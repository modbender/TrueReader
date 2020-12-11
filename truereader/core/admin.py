from django.contrib import admin

from . import models

class BaseCoreAdmin(admin.ModelAdmin):

    class Meta:
        abstract = True

    def get_form(self, request, obj=None, **kwargs):
        form = super(BaseCoreAdmin, self).get_form(request, obj, **kwargs)
        if 'user' in form.base_fields:
            form.base_fields['user'].initial = request.user
            form.base_fields['user'].disabled = True
        return form

@admin.register(models.Genre)
class GenreAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.Tag)
class TagAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.Cover)
class CoverAdmin(BaseCoreAdmin):
    search_fields = ['image']

@admin.register(models.Video)
class VideoAdmin(BaseCoreAdmin):
    search_fields = ['url']

@admin.register(models.Person)
class PersonAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.Publisher)
class PublisherAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.Magazine)
class MagazineAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.License)
class LicenseAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.Link)
class LinkAdmin(BaseCoreAdmin):
    search_fields = ['name']

@admin.register(models.Year)
class YearAdmin(BaseCoreAdmin):
    search_fields = ['number']

@admin.register(models.Comic)
class ComicAdmin(BaseCoreAdmin):
    autocomplete_fields = ['genres', 'tags', 'authors', 'artists', 'publishers', 'magazines', 'year', 'licenses', 'links']
