from django.db import models

class BaseSeoModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

TITLE_CHOICES = (
    ('short_site_name', 'Short site name'),
    ('full_site_name', 'Full site name'),
)

TWITTER_CARD_TYPE = (
    ('summary', 'Summary Card'),
    ('summary_large_image', 'Summary Card with Large Image')
)

class SeoDefault(BaseSeoModel):
    seperator = models.CharField(max_length=50, default='|')

    use_title = models.CharField(max_length=100, default='short_site_name', choices=TITLE_CHOICES)
    short_site_name = models.TextField()
    full_site_name = models.TextField(blank=True, null=True, help_text='Leave it empty if same as Short site name')

    description = models.TextField(blank=True, null=True)

    keywords = models.TextField(blank=True, null=True)

    # site_url = models.URLField(max_length=500, help_text='Something like http://www.example.com, only site url.')

    theme_color = models.CharField(max_length=50, default='#fff')

    twitter_card_type = models.CharField(max_length=100, default='summary', choices=TWITTER_CARD_TYPE)
    twitter_site_handle = models.TextField(blank=True, null=True, help_text='The Twitter @username the card should be attributed to.')

    google_analytics_id = models.CharField(max_length=100, blank=True, null=True, help_text='UA-XXXXXXXXX-X')

    extra_default_tags = models.TextField(blank=True, null=True, help_text='Seperate html tags by lines')

    @property
    def title(self):
        return getattr(self, self.use_title, self.short_site_name)

    @property
    def site_name(self):
        return self.full_site_name or self.short_site_name

    @property
    def extra_tags(self):
        return [t.strip() for t in self.extra_default_tags.split('\n')]
