# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.translations


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0003_auto_20180716_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageColors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Image color',
                'verbose_name_plural': 'Image colors',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ImageColorsTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.ImageColors')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
        migrations.CreateModel(
            name='ImageFormat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Image format',
                'verbose_name_plural': 'Image formats',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ImageFormatTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name (eg. 120x120cm)')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.ImageFormat')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
        migrations.CreateModel(
            name='ImageTechnique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Image technique',
                'verbose_name_plural': 'Image techniques',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ImageTechniqueTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name (eg. 120x120cm)')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.ImageTechnique')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
        migrations.CreateModel(
            name='ImageTheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Image theme',
                'verbose_name_plural': 'Image themes',
            },
            bases=(models.Model, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='ImageThemeTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'cs', max_length=10, verbose_name='language', choices=[(b'cs', b'CS'), (b'en', b'EN')])),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('parent', models.ForeignKey(related_name='translations', to='leonardo_module_art_folio.ImageTheme')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
        migrations.AlterModelOptions(
            name='imagecategory',
            options={'ordering': ['ordering'], 'verbose_name': 'Image category', 'verbose_name_plural': 'Image categories'},
        ),
        migrations.RemoveField(
            model_name='projectimagetranslation',
            name='size',
        ),
    ]
