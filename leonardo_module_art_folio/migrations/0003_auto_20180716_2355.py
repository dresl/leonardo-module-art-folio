# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0002_auto_20180716_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimagetranslation',
            name='description',
            field=models.TextField(default=b'', null=True, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='projectimagetranslation',
            name='size',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name='Size', blank=True),
        ),
        migrations.AlterField(
            model_name='projecttranslation',
            name='description',
            field=models.TextField(default=b'', null=True, verbose_name='Description', blank=True),
        ),
    ]
