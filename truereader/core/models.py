import os

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.functional import cached_property

from easy_thumbnails.fields import ThumbnailerImageField

PUBLISH_STATUS = (
    ('am', 'Awaiting Moderation'),
    ('p', 'Published'),
    ('r', 'Rejected'),
)

class UserControl:
    publishing_status = models.PositiveIntegerField(default='am', choices=PUBLISH_STATUS, db_index=True)
    published_at = models.DateTimeField(default=timezone.now, db_index=True)

    def get_published(self):
        return self.__class__.objects.filter(publishing_status='p')

class BaseCoreModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    added_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-modified_at']

    def __str__(self):
        return getattr(self, 'name', None) or\
            getattr(self, 'title', None) or\
            getattr(self, 'image', None) or\
            getattr(self, 'url', None)


    @cached_property
    def get_absolute_path(self):
        return reverse(self.__class__.__name__.lower(), self.id)

class Genre(BaseCoreModel):
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)

class Tag(BaseCoreModel):
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)

class Person(BaseCoreModel):
    name = models.TextField(unique=True)
    alt = models.TextField(verbose_name='Alternative Names', help_text='Seperate alternate names by new line', blank=True, null=True)

    def image_path(self, filename):
        return os.path.join('person', str(self.id), filename)

    image = ThumbnailerImageField(upload_to=image_path, blank=True, null=True)

class Cover(BaseCoreModel):

    def image_path(self, filename):
        return os.path.join('cover', str(self.id), filename)

    image = ThumbnailerImageField(upload_to=image_path)

class Video(BaseCoreModel):
    url = models.URLField(max_length=500)
    thumbnail_url = models.URLField(max_length=500)

class Year(BaseCoreModel):
    number = models.PositiveIntegerField(unique=True)

class License(BaseCoreModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    url = models.URLField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class LinkName(BaseCoreModel):

    def logo_path(self, filename):
        return os.path.join('linkname', str(self.id), filename)

    logo = models.ImageField(upload_to=logo_path, blank=True, null=True, max_length=150)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Link Names'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def logo_elem(self):
        if self.logo:
            return mark_safe('<img class="img-fluid" style="max-height:16px;" src="'+self.logo.url+'" alt="'+self.name+'" title="'+self.name+'"/>')
        else:
            return self.name

class Link(BaseCoreModel):
    name = models.ForeignKey(LinkName, on_delete=models.CASCADE)
    url = models.URLField(max_length=1000)

    def __str__(self):
        return str(self.name.name)

class Magazine(BaseCoreModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    alt = models.TextField(verbose_name='Alternative Names', help_text='Seperate alternate names by new line', blank=True, null=True)
    url = models.URLField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Publisher(BaseCoreModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    alt = models.TextField(verbose_name='Alternative Names', help_text='Seperate alternate names by new line', blank=True, null=True)
    url = models.URLField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

COMIC_LANGUAGES = (
    ('en', 'English'),
    ('jp', 'Japanese'),
    ('kr', 'Korean'),
    ('ch', 'Chinese'),
)

CHAPTER_LANGUAGES = COMIC_LANGUAGES[1:]

COMIC_TYPE = (
    (0, 'Manga'),
    (1, 'Manhwa'),
    (2, 'Manhua'),
    (3, 'Webtoon'),
    (4, 'Doujinshi'),
)

COMIC_STATUS = (
    (0, 'Ongoing'),
    (1, 'Haitus'),
    (2, 'Axed'),
    (3, 'Unknown'),
    (4, 'Finished'),
)

class Comic(BaseCoreModel):

    def background_path(self, filename):
        return os.path.join('background', str(self.id), filename)

    background_image = ThumbnailerImageField(upload_to=background_path, blank=True, null=True)
    cover = models.OneToOneField(Cover, on_delete=models.SET_NULL, blank=True, null=True, related_name='current_cover')
    title = models.TextField(unique=True)
    alt = models.TextField(verbose_name='Alternative Names', help_text='Seperate alternate names by new line', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    authors = models.ManyToManyField(Person, blank=True, related_name='authors')
    artists = models.ManyToManyField(Person, blank=True, related_name='artists')
    genres = models.ManyToManyField(Genre, blank=True, related_name='genres')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')
    publishers = models.ManyToManyField(Publisher, blank=True, related_name='publishers')
    magazines = models.ManyToManyField(Magazine, blank=True, related_name='magazines')
    licenses = models.ManyToManyField(License, blank=True, related_name='licenses')
    links = models.ManyToManyField(Link, blank=True, related_name='links')
    year = models.ForeignKey(Year, verbose_name='Release Year', on_delete=models.CASCADE, blank=True, null=True)

    #choice fields
    ctype = models.PositiveSmallIntegerField(choices=COMIC_TYPE)
    clang = models.CharField(max_length=50, choices=COMIC_LANGUAGES)
    cstatus = models.PositiveSmallIntegerField(choices=COMIC_STATUS)
    adult = models.BooleanField(default=False, db_index=True, help_text='Check if the manga is an adult/hentai manga')

class Chapter(BaseCoreModel):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='chapters', db_index=True)

    volume = models.FloatField(
        verbose_name='Volume Number', default=0, db_index=True, blank=True, null=True,
        help_text='Best to leave this as 0 if the chapter does not belong to any volumes'
    )
    number = models.CharField(
        verbose_name='Chapter Number', max_length=50,
        db_index=True, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, default='en', choices=CHAPTER_LANGUAGES)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Page(BaseCoreModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='pages')

    def image_path(self, filename):
        return os.path.join('page', str(self.id), filename)

    image = models.ImageField(upload_to=image_path)

class Blog(BaseCoreModel):
    pass
