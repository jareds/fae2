# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-12 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_websitereport_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitereport',
            name='domain',
            field=models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Domain'),
        ),
        migrations.AddField(
            model_name='websitereport',
            name='scheme',
            field=models.CharField(blank=True, default=b'http', max_length=16, verbose_name=b'Scheme'),
        ),
    ]