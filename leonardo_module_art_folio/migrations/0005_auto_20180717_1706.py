# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0004_auto_20180717_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='colors',
            field=models.ManyToManyField(to='leonardo_module_art_folio.ImageColors', null=True, verbose_name='Colors', blank=True),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='image_format',
            field=models.ManyToManyField(to='leonardo_module_art_folio.ImageFormat', null=True, verbose_name='Format', blank=True),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='technique',
            field=models.ManyToManyField(to='leonardo_module_art_folio.ImageTechnique', null=True, verbose_name='Technique', blank=True),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='theme',
            field=models.ManyToManyField(to='leonardo_module_art_folio.ImageTheme', null=True, verbose_name='Theme', blank=True),
        ),
    ]
