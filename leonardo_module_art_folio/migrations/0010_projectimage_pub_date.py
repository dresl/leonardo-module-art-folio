# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0009_projectimagetranslation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 24, 11, 23, 39, 365704, tzinfo=utc), verbose_name='Published on', auto_now_add=True),
            preserve_default=False,
        ),
    ]
