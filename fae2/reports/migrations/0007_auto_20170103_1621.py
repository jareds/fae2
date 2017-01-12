# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-03 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_websitereport_more_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitereport',
            name='require_path',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='websitereport',
            name='protocol',
            field=models.CharField(choices=[(b'http', b'http'), (b'https', b'https')], default=b'http', max_length=16, verbose_name=b'Protocol'),
        ),
    ]