# Generated by Django 3.1.3 on 2020-12-03 18:18

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('volume', models.FloatField(blank=True, db_index=True, default=0, help_text='Best to leave this as 0 if the chapter does not belong to any volumes', null=True, verbose_name='Volume Number')),
                ('number', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Chapter Number')),
                ('name', models.TextField(blank=True, null=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('jp', 'Japanese'), ('kr', 'Korean'), ('ch', 'Chinese')], default='en', max_length=50)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('number', models.PositiveIntegerField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('url', models.URLField(max_length=500)),
                ('thumbnail_url', models.URLField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('alt', models.TextField(blank=True, help_text='Seperate alternate names by new line', null=True, verbose_name='Alternative Names')),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(unique=True)),
                ('alt', models.TextField(blank=True, help_text='Seperate alternate names by new line', null=True, verbose_name='Alternative Names')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=core.models.Person.image_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('image', models.ImageField(upload_to=core.models.Page.image_path)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='core.chapter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('alt', models.TextField(blank=True, help_text='Seperate alternate names by new line', null=True, verbose_name='Alternative Names')),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LinkName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('logo', models.ImageField(blank=True, max_length=150, null=True, upload_to=core.models.LinkName.logo_path)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Link Names',
                'verbose_name_plural': 'Link Names',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('url', models.URLField(max_length=1000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.linkname')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=core.models.Cover.image_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('background_image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=core.models.Comic.background_path)),
                ('title', models.TextField(unique=True)),
                ('alt', models.TextField(blank=True, help_text='Seperate alternate names by new line', null=True, verbose_name='Alternative Names')),
                ('description', models.TextField(blank=True, null=True)),
                ('ctype', models.PositiveSmallIntegerField(choices=[(0, 'Manga'), (1, 'Manhwa'), (2, 'Manhua'), (3, 'Webtoon'), (4, 'Doujinshi')])),
                ('clang', models.CharField(choices=[('en', 'English'), ('jp', 'Japanese'), ('kr', 'Korean'), ('ch', 'Chinese')], default='en', max_length=50)),
                ('cstatus', models.PositiveSmallIntegerField(choices=[(0, 'Ongoing'), (1, 'Haitus'), (2, 'Axed'), (3, 'Unknown'), (4, 'Finished')])),
                ('adult', models.BooleanField(db_index=True, default=False, help_text='Check if the manga is an adult/hentai manga')),
                ('artists', models.ManyToManyField(blank=True, related_name='artists', to='core.Person')),
                ('authors', models.ManyToManyField(blank=True, related_name='authors', to='core.Person')),
                ('cover', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_cover', to='core.cover')),
                ('genres', models.ManyToManyField(blank=True, related_name='genres', to='core.Genre')),
                ('licenses', models.ManyToManyField(blank=True, related_name='licenses', to='core.License')),
                ('links', models.ManyToManyField(blank=True, related_name='links', to='core.Link')),
                ('magazines', models.ManyToManyField(blank=True, related_name='magazines', to='core.Magazine')),
                ('publishers', models.ManyToManyField(blank=True, related_name='publishers', to='core.Publisher')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='core.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.year', verbose_name='Release Year')),
            ],
            options={
                'ordering': ['-modified_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='comic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='core.comic'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
