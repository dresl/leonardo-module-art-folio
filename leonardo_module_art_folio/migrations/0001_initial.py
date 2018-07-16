# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.translations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Project category',
                'verbose_name_plural': 'Project categories',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ImageCategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.ImageCategory')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'project_images/', verbose_name='Project Image')),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured Image')),
                ('categories', models.ManyToManyField(to='leonardo_module_art_folio.ImageCategory', verbose_name=b'Categories')),
                ('project', models.ForeignKey(related_name='images', verbose_name='Project', to='leonardo_module_art_folio.Project')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Project Image',
                'verbose_name_plural': 'Project Images',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ProjectImageTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('description', models.TextField(default=b'', max_length=255, verbose_name='Description')),
                ('size', models.CharField(default=b'', max_length=255, verbose_name='Size')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.ProjectImage')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
        migrations.CreateModel(
            name='ProjectTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(default=b'', verbose_name='Description')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.Project')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
    ]
