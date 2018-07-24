# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagecategory',
            options={'ordering': ['ordering'], 'verbose_name': 'Project image category', 'verbose_name_plural': 'Project image categories'},
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='categories',
            field=models.ManyToManyField(to='leonardo_module_art_folio.ImageCategory', null=True, verbose_name=b'Categories', blank=True),
        ),
        migrations.AlterField(
            model_name='projectimagetranslation',
            name='description',
            field=models.TextField(default=b'', verbose_name='Description'),
        ),
    ]
