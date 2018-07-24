# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0005_auto_20180717_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='status',
            field=models.CharField(default=b'available', max_length=255, verbose_name=b'Status', choices=[(b'available', 'Available'), (b'reserve', 'Reserve'), (b'sell', 'Sell'), (b'copy', 'Make copy')]),
        ),
    ]
