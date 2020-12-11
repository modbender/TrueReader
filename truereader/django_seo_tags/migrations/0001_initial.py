# Generated by Django 3.1.3 on 2020-12-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeoDefaults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('seperator', models.CharField(default='|', max_length=50)),
                ('use_title', models.CharField(choices=[('short_site_name', 'Short site name'), ('full_site_name', 'Full site name')], default='short_site_name', max_length=100)),
                ('short_site_name', models.TextField()),
                ('full_site_name', models.TextField(blank=True, help_text='Leave it empty if same as Short site name', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('site_url', models.URLField(help_text='Something like http://www.example.com, only site url.', max_length=500)),
                ('theme_color', models.CharField(default='#fff', max_length=50)),
                ('twitter_card_type', models.CharField(choices=[('summary', 'Summary Card'), ('summary_large_image', 'Summary Card with Large Image')], default='summary', max_length=100)),
                ('google_analytics_id', models.CharField(blank=True, help_text='UA-XXXXXXXXX-X', max_length=100, null=True)),
                ('extra_default_tags', models.TextField(blank=True, help_text='Seperate html tags by lines', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]