# Generated by Django 3.1.4 on 2020-12-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_seo_tags', '0003_seodefault_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='seodefault',
            name='twitter_handle',
            field=models.TextField(blank=True, help_text='The Twitter @username the card should be attributed to.', null=True),
        ),
    ]
