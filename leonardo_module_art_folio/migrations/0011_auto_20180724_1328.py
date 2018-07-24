# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0010_projectimage_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Published on'),
        ),
    ]
