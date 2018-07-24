# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0008_auto_20180723_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimagetranslation',
            name='slug',
            field=models.SlugField(default=b'', verbose_name='Slug'),
        ),
    ]
