# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0011_auto_20180724_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True, help_text='Will be filled in automatically when picture gets published.', null=True, verbose_name='Published on', db_index=True),
        ),
    ]
