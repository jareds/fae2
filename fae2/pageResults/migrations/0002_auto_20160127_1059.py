# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pageResults', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageresult',
            options={'ordering': ['page_number'], 'verbose_name': 'Page Result', 'verbose_name_plural': 'Page Results'},
        ),
    ]