# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-03 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0015_auto_20170703_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitereport',
            name='max_pages',
            field=models.IntegerField(choices=[(5, b'    5 pages'), (10, b'   10 pages'), (25, b'   25 pages'), (50, b'   50 pages'), (100, b'  100 pages'), (200, b'  200 pages'), (400, b'  400 pages'), (800, b'  800 pages')], default=0, verbose_name=b'Evaluation Limited To'),
        ),
    ]
