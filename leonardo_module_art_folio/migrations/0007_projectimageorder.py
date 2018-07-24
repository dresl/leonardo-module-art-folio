# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_module_art_folio', '0006_projectimage_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImageOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('telephone', models.CharField(max_length=100, verbose_name='Telephone')),
                ('email', models.EmailField(default=b'', max_length=254, verbose_name='E-mail')),
                ('note', models.TextField(default=b'', verbose_name='Note', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Order date')),
                ('picture', models.ForeignKey(related_name='orderimage', verbose_name='Picture', to='leonardo_module_art_folio.ProjectImage')),
            ],
            options={
                'ordering': ['pub_date'],
                'verbose_name': 'Picture Order',
                'verbose_name_plural': 'Picture Orders',
            },
        ),
    ]
